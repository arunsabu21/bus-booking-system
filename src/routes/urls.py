from django.urls import path
from .views import get_available_routes

urlpatterns = [
    path("", get_available_routes, name="get-routes"),
]