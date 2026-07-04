from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import CitySerializer, CityListSerializer
from .services import get_cities, get_city_id


@api_view(["GET"])
@permission_classes([AllowAny])
def cities(request):
    city_list = get_cities()

    serializer = CityListSerializer(city_list, many=True)

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
