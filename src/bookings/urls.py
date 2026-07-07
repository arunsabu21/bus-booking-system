from django.urls import path
from .views import booking_list, booking_details

urlpatterns = [
    path("", booking_list, name="booking-list"),
    path("<uuid:booking_id>/", booking_details, name="booking-details"),
]