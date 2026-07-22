from .models import Route, RouteStop
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


def get_routes():
    return Route.objects.filter(is_active=True).order_by("created_at")


def get_route_by_id(route_id):
    route = Route.objects.filter(
        id=route_id,
        is_active=True,
    ).first()

    if not route:
        raise NotFound("Route not found.")

    return route


def get_route_stops(route_id):
    route = (
        Route.objects.select_related("source_city", "destination_city")
        .filter(id=route_id, is_active=True)
        .first()
    )

    if not route:
        raise NotFound("Route not found.")

    intermediate_stops = list(
        RouteStop.objects.select_related("city")
        .filter(route=route)
        .order_by("stop_order")
    )

    return {
        "route_id": route.id,
        "route_name": route.route_name,
        "source_city": route.source_city.name,
        "destination_city": route.destination_city.name,
        "stops": intermediate_stops,
    }
