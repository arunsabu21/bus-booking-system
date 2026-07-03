import uuid
from django.db import models

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "City"
        verbose_name_plural = "Cities"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "state"],
                name="unique_city_state",
            )
        ]
    
    def __str__(self):
        return f"{self.name}, {self.state}"