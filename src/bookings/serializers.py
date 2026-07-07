from rest_framework import serializers
from .models import Booking


class BookingListSerializer(serializers.ModelSerializer):
    trip = serializers.CharField(source="trip.route.route_name")
    user = serializers.CharField(source="user.email")

    class Meta:
        model = Booking
        fields = [
            "id",
            "booking_reference",
            "user",
            "trip",
            "seat_count",
            "total_amount",
            "status",
        ]


class BookingSerializer(serializers.ModelSerializer):
    trip = serializers.CharField(source="trip.route.route_name")
    user = serializers.CharField(source="user.email")

    class Meta:
        model = Booking
        fields = [
            "id",
            "booking_reference",
            "user",
            "trip",
            "seat_count",
            "total_amount",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "booking_reference",
            "user",
            "total_amount",
            "status",
            "created_at",
            "updated_at",
        ]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "trip",
            "seat_count",
        ]