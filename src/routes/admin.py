from django.contrib import admin

from .models import Route, RouteStop


class RouteStopInline(admin.TabularInline):
    model = RouteStop
    extra = 1


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        "route_code",
        "route_name",
        "source_city",
        "destination_city",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "route_code",
        "route_name",
        "source_city__name",
        "destination_city__name",
    )

    ordering = (
        "route_name",
    )

    inlines = [
        RouteStopInline,
    ]


@admin.register(RouteStop)
class RouteStopAdmin(admin.ModelAdmin):
    list_display = (
        "route",
        "city",
        "stop_order",
    )

    list_filter = (
        "route",
    )

    search_fields = (
        "route__route_name",
        "city__name",
    )

    ordering = (
        "route",
        "stop_order",
    )