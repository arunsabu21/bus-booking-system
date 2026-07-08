from django.urls import path
from .views import booking_list, booking_details, booking_create

urlpatterns = [
    path("", booking_list, name="booking-list"),
    path("<uuid:booking_id>/", booking_details, name="booking-details"),
    path("create/", booking_create, name="booking-create"),
]