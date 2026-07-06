from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import TripListSerializer, TripSerializer
from .services import get_trips, get_trip_by_id


@api_view(["GET"])
@permission_classes([AllowAny])
def list_trips(request):
    trips = get_trips()

    serializer = TripListSerializer(trips, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def trip_details(request, trip_id):
    trip = get_trip_by_id(trip_id)

    serializer = TripSerializer(trip)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )