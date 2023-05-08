from django.urls import path
from .views import *

urlpatterns = [
    #path('asignar_lugar/', asignar_lugar_view, name='asignar_lugar'),
    path('detalleLugar/', detalleLugar, name='detalleLugar'),
]