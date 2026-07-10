from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import CitySerializer, CityListSerializer
from .services import get_cities, get_city_id

from core.cache.keys import cities_list_key
from core.cache.services import get_cache, set_cache
from core.constants.cache import CITY_LIST_CACHE_TIMEOUT


@api_view(["GET"])
@permission_classes([AllowAny])
def cities(request):
    cache_key = cities_list_key()

    cached_response = get_cache(cache_key)

    if cached_response is not None:
        return Response(
            cached_response,
            status=status.HTTP_200_OK,
        )
    
    city_list = get_cities()

    serializer = CityListSerializer(city_list, many=True)

    set_cache(
        key=cache_key,
        value=serializer.data,
        timeout=CITY_LIST_CACHE_TIMEOUT,
    )

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def city_details(request, city_id):
    city = get_city_id(city_id)

    serializer = CitySerializer(city)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
