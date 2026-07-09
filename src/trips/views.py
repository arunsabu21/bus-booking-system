from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import TripListSerializer, TripSerializer, TripSearchSerializer
from .services import get_trips, get_trip_by_id, search_trips, get_trip_seats


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


@api_view(["GET"])
@permission_classes([AllowAny])
def trip_search(request):
    source = request.query_params.get("source")
    destination = request.query_params.get("destination")
    travel_date = request.query_params.get("travel_date")

    trips = search_trips(
        source=source, destination=destination, travel_date=travel_date
    )

    serializer = TripSearchSerializer(trips, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def trip_seats(request, trip_id):
    seats = get_trip_seats(trip_id=trip_id)

    return Response(
        seats,
        status=status.HTTP_200_OK,
    )
