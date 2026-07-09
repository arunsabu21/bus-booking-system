from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    BookingListSerializer,
    BookingSerializer,
    BookingCreateSerializer,
)

from .services import (
    get_bookings,
    get_booking_details,
    create_booking,
    cancel_booking,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def booking_list(request):
    bookings = get_bookings(request.user)

    serializer = BookingListSerializer(bookings, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def booking_details(request, booking_id):
    booking = get_booking_details(user=request.user, booking_id=booking_id)

    serializer = BookingSerializer(booking)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def booking_create(request):
    serializer = BookingCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    booking = create_booking(
        user=request.user,
        trip_id=serializer.validated_data["trip"].id,
        seat_numbers=serializer.validated_data["seat_numbers"],
    )

    response_serializer = BookingSerializer(booking)

    return Response(
        response_serializer.data,
        status=status.HTTP_201_CREATED,
    )


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def booking_cancel(request, booking_id):
    cancel = cancel_booking(user=request.user, booking_id=booking_id)

    serializer = BookingSerializer(cancel)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
