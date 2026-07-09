from django.urls import path
from .views import list_trips, trip_details, trip_search, trip_seats

urlpatterns = [
    path("", list_trips, name="trips"),
    path("<uuid:trip_id>/", trip_details, name="trip-details"),
    path("search/", trip_search, name="trip-search"),
    path("<uuid:trip_id>/seats/", trip_seats, name="trip-seats"),
]