from .models import City
from rest_framework.exceptions import ValidationError


def get_cities():
    cities = City.objects.filter(is_active=True).order_by("created_at")

    if not cities.exists():
        raise ValidationError("Cities not found.")

    return cities


def get_city_id(city_id):
    try:
        city = City.objects.get(id=city_id, is_active=True)

        return city

    except City.DoesNotExist:
        raise ValidationError("City not found.")
