from rest_framework import serializers
from .models import Trip
from buses.serializers import BusSerializer


class TripSerializer(serializers.ModelSerializer):
    route = serializers.CharField(source="route.route_name")
    route_id = serializers.UUIDField(source="route.id", read_only=True)
    bus = BusSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = [
            "id",
            "route",
            "route_id",
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


class TripSearchSerializer(serializers.ModelSerializer):
    operator = serializers.CharField(source="bus.operator.company_name")
    bus = serializers.CharField(source="bus.bus_name")
    route = serializers.CharField(source="route.route_name")

    class Meta:
        model = Trip
        fields = [
            "id",
            "operator",
            "bus",
            "route",
            "travel_date",
            "departure_time",
            "arrival_time",
            "fare",
            "available_seats",
        ]
