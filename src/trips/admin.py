from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        "travel_date",
        "route",
        "bus",
        "departure_time",
        "arrival_time",
        "fare",
        "available_seats",
        "status",
        "is_active",
    )

    list_filter = (
        "status",
        "travel_date",
        "is_active",
    )

    search_fields = (
        "route__route_name",
        "bus__bus_number",
        "bus__registration_number",
    )

    ordering = (
        "travel_date",
        "departure_time",
    )