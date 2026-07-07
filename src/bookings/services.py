from rest_framework.exceptions import NotFound
from .models import Booking


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
