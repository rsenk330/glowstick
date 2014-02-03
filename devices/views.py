from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from libhdhomerun import get_devices
from .serializers import DeviceSerializer


class Device(ReadOnlyModelViewSet):
    lookup_field = "id"
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return get_devices()

    def get_object(self):
        queryset = self.get_queryset()
        return next((d for d in queryset if d.id == self.kwargs["id"]), None)
