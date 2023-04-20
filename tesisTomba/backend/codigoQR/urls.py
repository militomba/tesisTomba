from django.views.generic import base
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'codigoQR', codigoQR, basename='codigoQR')
urlpatterns = router.urls