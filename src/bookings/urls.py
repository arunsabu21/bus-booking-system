from django.urls import path
from .views import (
    booking_list,
    booking_details,
    booking_create,
    booking_cancel,
)

urlpatterns = [
    path("", booking_list, name="booking-list"),
    path("<uuid:booking_id>/", booking_details, name="booking-details"),
    path("create/", booking_create, name="booking-create"),
    path("<uuid:booking_id>/cancel/", booking_cancel, name="booking-cancel"),
]