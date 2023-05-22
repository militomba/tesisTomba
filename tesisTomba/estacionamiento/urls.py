from django.urls import path
from .views import *

urlpatterns = [
    #path('asignar_lugar/', asignar_lugar_view, name='asignar_lugar'),
    path('detalleLugar/', Funciones.detalleLugar, name='detalleLugar'),
    path('liberarLugar/<str:lugar>/', Funciones.liberarLugar, name='liberarLugar'),
    path('cc/<str:nombre>/', Funciones.centroComercial, name='cc'),
    #centrosComerciales
    path('centroComercial/', CentrosComercialesViews.listCentroComercial, name='centroComercial'),
    path('centroComercial/<str:nombre>/', CentrosComercialesViews.detalle_centro, name='detalle_centro'),
    path('crearCentroComercial/', CentrosComercialesViews.crearCentroComercial, name='crearCentroComercial'),
    path('eliminarCentro/<str:nombre>/', CentrosComercialesViews.eliminarCentroComerial, name='eliminarCentro'),
    path('edicionCentro/<str:nombre>/', CentrosComercialesViews.edicionCentroComercial, name='edicionCentro')

]