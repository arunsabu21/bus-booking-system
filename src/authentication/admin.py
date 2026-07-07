from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "phone_number",
        "is_verified",
        "is_active",
        "is_staff",
        "created_at",
    )

    list_filter = (
        "is_verified",
        "is_active",
        "is_staff",
        "created_at",
    )

    search_fields = (
        "email",
        "full_name",
        "phone_number",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "last_login",
    )

    ordering = ("-created_at",)
