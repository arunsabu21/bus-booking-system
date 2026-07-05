from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import RouteSerializer
from .services import get_routes


@api_view(["GET"])
@permission_classes([AllowAny])
def get_available_routes(request):

    routes = get_routes()

    serializer = RouteSerializer(routes, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
