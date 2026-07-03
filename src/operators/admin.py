from django.contrib import admin
from .models import Operator


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "company_code",
        "support_email",
        "headquarters",
        "is_active",
    )

    search_fields = (
        "company_name",
        "company_code",
    )

    list_filter = ("is_active",)

    ordering = ["company_name"]
