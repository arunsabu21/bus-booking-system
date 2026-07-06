from .models import Route
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


def get_routes():
    routes = Route.objects.filter(is_active=True).order_by("created_at")

    if not routes.exists():
        raise NotFound("Routes not found.")
    
    return routes


def get_route_by_id(route_id):
    route = Route.objects.filter(
        id=route_id,
        is_active=True,
    ).first()

    if not route:
        raise NotFound("Route not found.")
    
    return route