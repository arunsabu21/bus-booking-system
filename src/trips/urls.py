from django.urls import path
from .views import list_trips, trip_details

urlpatterns = [
    path("", list_trips, name="trips"),
    path("<uuid:trip_id>/", trip_details, name="trip-details"),
]