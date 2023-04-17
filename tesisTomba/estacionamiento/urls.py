from django.views.generic import base
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'centroComercial', centroComercialViewSet, basename='centroComercial')

urlpatterns = router.urls