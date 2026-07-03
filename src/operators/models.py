import uuid
from django.db import models


class Operator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100, unique=True)
    company_code = models.CharField(max_length=10, unique=True)
    support_email = models.EmailField(unique=True)
    support_phone = models.CharField(max_length=15, unique=True)
    headquarters = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["company_name"]
        verbose_name = "Operator"
        verbose_name_plural = "Operators"

    def __str__(self):
        return self.company_name