from .models import Bus
from rest_framework.exceptions import ValidationError

def get_bus():
    bus = Bus.objects.filter(is_active=True).order_by("created_at")

    if not bus.exists():
        raise ValidationError("Buses not found.")
    
    return bus


def get_bus_by_id(bus_id):
    try:
        bus = Bus.objects.get(
            id=bus_id,
            is_active=True
        )

        return bus
    
    except Bus.DoesNotExist:
        raise ValidationError("Bus not found.")