from rest_framework import serializers
from .models import Device, DeviceValue

class DeviceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceValue
        fields = ['id', 'timestamp', 'temperature', 'humidity']

class DeviceSerializer(serializers.ModelSerializer):
    values = DeviceValueSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'serial_number','location','status', 'values']