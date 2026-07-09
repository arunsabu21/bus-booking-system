from rest_framework.exceptions import ValidationError, NotFound
from .models import Trip
from bookings.models import SeatBooking


def get_trips():
    trips = Trip.objects.filter(
        is_active=True,
    ).order_by("travel_date", "departure_time")

    if not trips.exists():
        return NotFound("Trips not found.")

    return trips


def get_trip_by_id(trip_id):
    try:
        return Trip.objects.get(
            id=trip_id,
            is_active=True,
        )
    
    except Trip.DoesNotExist:
        raise NotFound("Trip not found.")


def search_trips(*, source, destination, travel_date):
    if not source:
        raise ValidationError("Source city is required.")
    
    if not destination:
        raise ValidationError("Destination city is required.")
    
    if not travel_date:
        raise ValidationError("Travel date is required.")
    
    return (
        Trip.objects.select_related(
            "route",
            "route__source_city",
            "route__destination_city",
            "bus",
            "bus__operator",
        ).filter(
            is_active=True,
            status=Trip.Status.SCHEDULED,
            route__source_city__name__iexact=source,
            route__destination_city__name__iexact=destination,
            travel_date=travel_date,
        ).order_by("departure_time")
    )


def get_trip_seats(trip_id):
    try:
        trip = Trip.objects.select_related("bus").get(
            id=trip_id,
            is_active=True,
        )

    except Trip.DoesNotExist:
        raise NotFound("Trip not found.")

    booking_seats = set(
        SeatBooking.objects.filter(
            trip=trip,
        ).values_list(
            "seat_number",
            flat=True,
        )
    )

    seats = []

    for seat_number in range(1, trip.bus.total_seats + 1):
        seat = f"S{seat_number}"

        seats.append(
            {
                "seat_number": seat,
                "status": ("BOOKED" if seat in booking_seats else "AVAILABLE"),
            }
        )
    
    return {
        "trip": trip.route.route_name,
        "available_seats": trip.available_seats,
        "total_seats": trip.bus.total_seats,
        "seats": seats,
    }