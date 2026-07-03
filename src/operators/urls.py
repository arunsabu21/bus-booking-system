from django.urls import path
from .views import operator_list, operator_detail

urlpatterns = [
    path("", operator_list, name="operator-list"),
    path("<uuid:operator_id>/", operator_detail, name="operator-detail"),
]