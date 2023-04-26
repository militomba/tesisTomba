from django.views.generic import base
from rest_framework import routers
from .views import *
from django.urls import path



urlpatterns = [
    # ...
    # path('home/', CodigoQRLugar.home_view, name='home'),
    # path('generar/', generarCodigoQR, name='generar'),
    # path('<int:codigoqr_id>/', ver_codigoqr, name='ver'),
    path('index/', index, name='index')
]