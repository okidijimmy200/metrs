from django.shortcuts import render
from rest_framework import viewsets
from .models import Device
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from .serializer import DeviceSerializer, DeviceValueSerializer, DeviceValue
from drf_spectacular.utils import extend_schema_view, OpenApiParameter
from rest_framework.response import Response
from rest_framework.decorators import action


@extend_schema(tags=['Devices'])
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['get'])
    def values(self, request, pk=None):
        device = self.get_object()
        values = DeviceValue.objects.filter(device=device)
        serializer = DeviceValueSerializer(values, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def addvalue(self, request, pk=None):
        device = self.get_object()
        if "device" not in request.data:
            request.data['device'] = device.id
        value_serializer = DeviceValueSerializer(data=request.data)
        value_serializer.is_valid(raise_exception=True)
        value_serializer.save()

        return Response(value_serializer.data)