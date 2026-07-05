from rest_framework import serializers
from .models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            "id",
            "route_code",
            "route_name",
            "source_city",
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