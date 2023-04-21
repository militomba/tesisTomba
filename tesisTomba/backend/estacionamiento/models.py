from django.conf import settings
from codigoQR.models import *

from django.db import models

class CentroComercialEspecifico(models.Model):
    nombre = models.CharField(max_length=200)
    lugares = models.IntegerField(default=0)
    niveles = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)
    qrCentroComercial = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False)

class Lugares(models.Model):
    lugar = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    nivel = models.CharField(max_length=30)
    id_cc = models.ForeignKey(CentroComercialEspecifico, on_delete=models.CASCADE, null=False, related_name='lugares_cc')

class Estacionamiento(models.Model):
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    lugar = models.ForeignKey(Lugares, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    qrLugarAsignado = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False, related_name='cQR')
    
    





    



