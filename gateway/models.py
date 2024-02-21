from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Device(BaseModel):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    class Meta:
        app_label = 'gateway'

    def __str__(self):
        return self.name
    
class DeviceValue(BaseModel):
        device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='values')
        temperature = models.FloatField()
        humidity = models.FloatField()
        timestamp = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return f"{self.device} - {self.temperature}C, {self.humidity}% ({self.timestamp})"
