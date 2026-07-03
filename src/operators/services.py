from .models import Operator
from rest_framework.exceptions import ValidationError


def get_operators():
    operators = Operator.objects.filter(is_active=True).order_by("created_at")

    if not operators.exists():
        raise ValidationError("Operators not found")

    return operators


def get_operator_by_id(operator_id):
    try:
        operator = Operator.objects.get(
            id=operator_id,
            is_active=True
        )

        return operator
    
    except Operator.DoesNotExist:
        raise ValidationError("Operator not found.")
