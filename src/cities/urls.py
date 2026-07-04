from django.urls import path
from .views import cities, city_details

urlpatterns = [
    path("", cities, name="city-list"),
    path("<uuid:city_id>/", city_details, name="city-details"),
]