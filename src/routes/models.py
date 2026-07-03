import uuid
from django.db import models
from cities.models import City


class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route_code = models.CharField(max_length=20, unique=True)
    route_name = models.CharField(max_length=150)
    source_city = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name="source_routes"
    )
    destination_city = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name="destination_routes"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["route_name"]
        verbose_name = "Route"
        verbose_name_plural = "Routes"

    def __str__(self):
        return self.route_name


class RouteStop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="stops")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="route_stops")
    stop_order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["route", "stop_order"]
        verbose_name = "Route Stop"
        verbose_name_plural = "Route Stops"
        constraints = [
            models.UniqueConstraint(
                fields=["route", "stop_order"],
                name="unique_route_stop_order",
            )
        ]

    def __str__(self):
        return f"{self.route.route_name} - {self.city.name}"
