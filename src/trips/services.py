from rest_framework.exceptions import ValidationError, NotFound
from .models import Trip


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