from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import OperatorListSerializer, OperatorSerializer
from .services import get_operators, get_operator_by_id


@api_view(["GET"])
@permission_classes([AllowAny])
def operator_list(request):
    operators = get_operators()

    serializer = OperatorListSerializer(operators, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def operator_detail(request, operator_id):
    operator = get_operator_by_id(operator_id)

    serializer = OperatorSerializer(operator)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
