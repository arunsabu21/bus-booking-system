from rest_framework.exceptions import ValidationError, NotFound
from .models import Trip
from bookings.models import SeatBooking
from datetime import datetime


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
    
    try:
        parsed_date = datetime.strptime(travel_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Invalid travel date format. Use YYYY-MM-DD.")
    
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
            travel_date=parsed_date,
        ).order_by("departure_time")
    )

def _parse_seat_layout(seat_layout):
    try:
        left, right = seat_layout.split("+")
        return int(left), int(right)
    except (ValueError, AttributeError):
        return 2, 2


def _generate_deck_seats(prefix, seat_count, seat_layout):
    left_count, right_count = _parse_seat_layout(seat_layout)
    seats_per_row = left_count + right_count

    labels = []
    seat_number = 1
    while len(labels) < seat_count:
        for _ in range(seats_per_row):
            if len(labels) >= seat_count:
                break
            labels.append(f"{prefix}{seat_number}")
            seat_number += 1

    return labels


def get_trip_seats(trip_id):
    try:
        trip = Trip.objects.select_related("bus").get(
            id=trip_id,
            is_active=True,
        )

    except Trip.DoesNotExist:
        raise NotFound("Trip not found.")

    bus = trip.bus
    booking_seats = set(
        SeatBooking.objects.filter(
            trip=trip,
        ).values_list(
            "seat_number",
            flat=True,
        )
    )

    if bus.deck_count == bus.Deck.DOUBLE:
        half = bus.total_seats // 2
        lower_count = half
        upper_count = bus.total_seats - half

        seat_labels = _generate_deck_seats(
            "L", lower_count, bus.seat_layout
        ) + _generate_deck_seats("U", upper_count, bus.seat_layout)
    else:
        seat_labels = _generate_deck_seats(
            "S", bus.total_seats, bus.seat_layout
        )

    seats = [
        {
            "seat_number": label,
            "deck": "LOWER" if label.startswith("L") else "UPPER" if label.startswith("U") else "MAIN",
            "status": "BOOKED" if label in booking_seats else "AVAILABLE",
        }
        for label in seat_labels
    ]

    return {
        "trip": trip.route.route_name,
        "available_seats": trip.available_seats,
        "total_seats": bus.total_seats,
        "seat_layout": bus.seat_layout,
        "deck_count": bus.deck_count,
        "seats": seats,
    }