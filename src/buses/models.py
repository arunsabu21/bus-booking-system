import uuid
from django.db import models
from operators.models import Operator


class Bus(models.Model):
    class BusType(models.TextChoices):
        AC_SEATER = "AC_SEATER", "AC Seater"
        AC_SLEEPER = "AC_SLEEPER", "AC Sleeper"
        NON_AC_SEATER = "NON_AC_SEATER", "Non-AC Seater"
        NON_AC_SLEEPER = "NON_AC_SLEEPER", "Non-AC Sleeper"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT, related_name="buses")
    bus_number = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=20, unique=True)
    bus_name = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=20, choices=BusType.choices)
    total_seats = models.PositiveSmallIntegerField()
    amenities = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = "Buses"
        ordering = ["bus_number"]

    def __str__(self):
        return f"{self.bus_number}({self.operator.company_name})"