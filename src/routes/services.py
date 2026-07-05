from .models import Route
from rest_framework.exceptions import NotFound


def get_routes():
    routes = Route.objects.filter(is_active=True).order_by("created_at")

    if not routes.exists():
        raise NotFound("Routes not found.")
    
    return routes