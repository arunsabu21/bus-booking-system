from rest_framework import serializers
from .models import Bus


class BusSerializer(serializers.ModelSerializer):
    operator = serializers.CharField(source="operator.company_name")

    class Meta:
        model = Bus
        fields = [
            "id",
            "operator",
            "bus_number",
            "registration_number",
            "bus_name",
            "bus_type",
            "total_seats",
            "amenities",
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


class BusListSerializer(serializers.ModelSerializer):
    operator = serializers.CharField(source="operator.company_name")

    class Meta:
        model = Bus
        fields = [
            "id",
            "operator",
            "bus_number",
            "bus_name",
            "bus_type",
            "total_seats",
            "amenities",
        ]
