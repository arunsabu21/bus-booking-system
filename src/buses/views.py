from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import BusSerializer, BusListSerializer
from .services import get_bus, get_bus_by_id

from core.cache.keys import get_buses_list_key
from core.cache.services import get_cache, set_cache
from core.constants.cache import BUS_LIST_CACHE_TIMEOUT


@api_view(["GET"])
@permission_classes([AllowAny])
def bus_list(request):
    cache_key = get_buses_list_key()
    cached_response = get_cache(cache_key)

    if cached_response is not None:
        return Response(
            cached_response,
            status=status.HTTP_200_OK,
        )
    
    buses = get_bus()

    serializer = BusListSerializer(buses, many=True)

    set_cache(
        key=cache_key,
        value=serializer.data,
        timeout=BUS_LIST_CACHE_TIMEOUT,
    )

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def bus_detail(request, bus_id):
    bus = get_bus_by_id(bus_id)

    serializer = BusSerializer(bus)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
