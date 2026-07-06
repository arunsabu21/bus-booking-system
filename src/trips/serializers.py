from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    route = serializers.CharField(source="route.route_name")
    bus = serializers.CharField(source="bus.bus_number")

    class Meta:
        model = Trip
        fields = [
            "id",
            "route",
            "bus",
            "travel_date",
            "departure_time",
            "arrival_time",
            "fare",
            "available_seats",
            "status",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "is_active",
            "created_at",
            "updated_at",
        ]


class TripListSerializer(serializers.ModelSerializer):
    route = serializers.CharField(source="route.route_name")
    bus = serializers.CharField(source="bus.bus_number")

    class Meta:
        model = Trip
        fields = [
            "id",
            "route",
            "bus",
            "travel_date",
            "departure_time",
            "arrival_time",
            "fare",
            "available_seats",
            "status",
        ]
