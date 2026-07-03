from rest_framework import serializers
from django.core.validators import RegexValidator

from .models import Operator


class OperatorSerializer(serializers.ModelSerializer):
    support_phone = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^[6-9]\d{9}$",
                message="Enter a valid 10-digit Indian mobile number",
            )
        ]
    )

    class Meta:
        model = Operator
        fields = [
            "id",
            "company_name",
            "company_code",
            "support_email",
            "support_phone",
            "headquarters",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "company_code",
            "is_active",
            "created_at",
            "updated_at",
        ]


class OperatorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ["id", "company_name", "company_code"]
