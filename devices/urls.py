from django.conf.urls import patterns, url, include
from rest_framework import routers

from .views import Device

router = routers.DefaultRouter()
router.register(r'devices', Device, base_name='devices')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
