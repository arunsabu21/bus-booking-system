from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookingListSerializer, BookingSerializer
from .services import get_bookings, get_booking_details


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
