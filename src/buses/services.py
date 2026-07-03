from .models import Bus

def get_bus():
    return Bus.objects.filter(
        is_active=True
    ).order_by("created_at")