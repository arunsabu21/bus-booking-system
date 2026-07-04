from django.urls import path
from .views import bus_list, bus_detail

urlpatterns = [
    path("", bus_list, name="buses"),
    path("<uuid:bus_id>/", bus_detail, name="bus-details"),
]