from django.conf import settings
from django.dispatch import receiver
from codigoQR.models import *
from django.db.models.signals import post_save

from django.db import models

class CentroComercialEspecifico(models.Model):
    nombre = models.CharField(max_length=200)
    cantidadLugares = models.IntegerField(default=0)
    niveles = models.IntegerField(default=0)
    qr = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False, related_name='codigoqr')

class Lugares(models.Model):
    lugar = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    nivel = models.CharField(max_length=30)
    id_cc = models.ForeignKey(CentroComercialEspecifico, on_delete=models.CASCADE, null=False, related_name='lugares_cc')


class LugaresOcupados(models.Model):
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    lugar = models.ForeignKey(Lugares, on_delete=models.CASCADE)
    qr_code = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False, related_name='cQR')
    available= models.BooleanField(default=True)
    
@receiver(post_save, sender=LugaresOcupados)
def actualizarDisponibilidad(sender, instance, **kwargs):
    if instance.available:
        ocupado = instance.lugar
        ocupado.status = False
        ocupado.save()
    





    



