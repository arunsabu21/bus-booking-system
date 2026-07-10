from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import OperatorListSerializer, OperatorSerializer
from .services import get_operators, get_operator_by_id

from core.cache.keys import operators_list_key
from core.cache.services import get_cache, set_cache
from core.constants.cache import OPERATOR_LIST_CACHE_TIMEOUT


@api_view(["GET"])
@permission_classes([AllowAny])
def operator_list(request):
    cache_key = operators_list_key()
    cached_response = get_cache(cache_key)

    if cached_response is not None:
        return Response(
            cached_response,
            status=status.HTTP_200_OK,
        )
    
    operators = get_operators()

    serializer = OperatorListSerializer(operators, many=True)

    set_cache(
        key=cache_key,
        value=serializer.data,
        timeout=OPERATOR_LIST_CACHE_TIMEOUT,
    )

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
