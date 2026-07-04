from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import BusSerializer, BusListSerializer
from .services import get_bus, get_bus_by_id


@api_view(["GET"])
@permission_classes([AllowAny])
def bus_list(request):
    buses = get_bus()

    serializer = BusListSerializer(buses, many=True)

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
