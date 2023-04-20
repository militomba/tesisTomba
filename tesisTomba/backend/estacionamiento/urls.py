from django.views.generic import base
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'centroComercial', centroComercialViewSet, basename='centroComercial')
router.register(r'lugares', LugaresViewSet, basename='lugares')
router.register(r'estacionamiento', EstacionamientoViewSet, basename='estacionamiento')
urlpatterns = router.urls