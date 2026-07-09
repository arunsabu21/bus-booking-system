import uuid
from decimal import Decimal
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError

from .models import Booking, SeatBooking
from trips.models import Trip


def get_bookings(user):
    return (
        Booking.objects.select_related(
            "trip",
            "trip__route",
        )
        .filter(user=user)
        .order_by("-created_at")
    )


def get_booking_details(user, booking_id):
    try:
        return Booking.objects.select_related(
            "trip",
            "trip__route",
        ).get(id=booking_id, user=user)

    except Booking.DoesNotExist:
        raise NotFound("Booking not found.")


@transaction.atomic
def create_booking(*, user, trip_id, seat_numbers):
    try:
        trip = Trip.objects.select_for_update().get(
            id=trip_id,
            is_active=True,
        )
    except Trip.DoesNotExist:
        raise NotFound("Trip not found.")

    if trip.status != Trip.Status.SCHEDULED:
        raise ValidationError("Trip is not available for booking.")

    seat_count = len(seat_numbers)

    if seat_count == 0:
        raise ValidationError("Select at least one seat.")
    
    valid_seats = {
        f"S{number}" for number in range(1, trip.bus.total_seats + 1)
    }

    invalid_seats = [
        seat
        for seat in seat_numbers
        if seat not in valid_seats
    ]

    if invalid_seats:
        raise ValidationError(f"Invalid seat numbers(s): {','.join(invalid_seats)}")
    
    booked_seats = set(
        SeatBooking.objects.filter(
            trip=trip,
            seat_number__in=seat_numbers,
        ).values_list("seat_number", flat=True)
    )

    if booked_seats:
        raise ValidationError(f"Seat(s) already booked: {','.join(sorted(booked_seats))}")

    if seat_count > trip.available_seats:
        raise ValidationError("Not enough seats available.")

    total_amount = Decimal(seat_count) * trip.fare

    booking = Booking.objects.create(
        booking_reference=generate_booking_reference(),
        user=user,
        trip=trip,
        seat_count=seat_count,
        total_amount=total_amount,
        status=Booking.Status.CONFIRMED,
    )

    SeatBooking.objects.bulk_create(
        [
            SeatBooking(
                booking=booking,
                trip=trip,
                seat_number=seat_number,
            )
            for seat_number in seat_numbers
        ]
    )

    trip.available_seats -= seat_count
    trip.save(update_fields=["available_seats"])

    return booking


def generate_booking_reference():
    while True:
        reference = f"BK-{uuid.uuid4().hex[:8].upper()}"

        if not Booking.objects.filter(booking_reference=reference).exists():
            return reference


@transaction.atomic
def cancel_booking(*, user, booking_id):
    booking = Booking.objects.select_related(
        "trip",
    ).get(id=booking_id, user=user)

    if booking.status == Booking.Status.CANCELLED:
        raise ValidationError("Booking is already cancelled.")

    if booking.trip.status == Trip.Status.COMPLETED:
        raise ValidationError("Completed trips cannot be cancelled.")

    trip = Trip.objects.select_for_update().get(id=booking.trip.id)

    trip.available_seats += booking.seat_count
    trip.save(update_fields=["available_seats"])

    booking.status = Booking.Status.CANCELLED
    booking.save(update_fields=["status"])

    SeatBooking.objects.filter(
        booking=booking,
    ).delete()

    return booking
