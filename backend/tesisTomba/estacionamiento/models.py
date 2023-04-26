from django.conf import settings
from django.dispatch import receiver
from codigoQR.models import *
from django.db.models.signals import post_save

from django.db import models

from codigoQR.models import CodigoQR

class CentroComercialEspecifico(models.Model):
    nombre = models.CharField(max_length=200)
    cantidadLugares = models.IntegerField(default=0)
    niveles = models.IntegerField(default=0)
    qr = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False, related_name='codigoqr')

    def __str__(self):
        return(self.nombre)
    
    def save(self,*args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

class Lugares(models.Model):
    lugar = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    nivel = models.CharField(max_length=30)
    id_cc = models.ForeignKey(CentroComercialEspecifico, on_delete=models.CASCADE, null=False, related_name='lugares_cc')

    def __str__(self):
        return ("Lugar: " + self.lugar + " Nivel: " + self.nivel)
    

    
    @staticmethod
    def lugaresDisponibles():
        lugaresDisponibles = Lugares.objects.filter(status=True)
        return lugaresDisponibles
    

class LugaresOcupados(models.Model):
    fecha = models.DateField(null=True, blank=True)
    hora_entrada = models.TimeField(null=True, blank=True)
    #hora_salida = models.DateTimeField(null=True, blank=True)
    id_lugar = models.ForeignKey(Lugares, on_delete=models.CASCADE)
    qr_code = models.ForeignKey(CodigoQR, on_delete=models.CASCADE, null=False, related_name='cQR')
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return ("Lugar: " + self.id_lugar.lugar)
    
    #no me deja crear dos lugares ocupados con el mismo lugar, pero si me deja modificarlo
    def save(self, **args):
        if not self.pk:
            if self.id_lugar.status!=True:
                raise ValueError("The associated Lugares object is not available.")   
        super().save(*args)
            


        
@receiver(post_save, sender=LugaresOcupados)
def actualizarDisponibilidad(sender, instance, **kwargs):
    if instance.available == True:
        ocupado = instance.id_lugar
        ocupado.status = False
        ocupado.save()
    else:
        ocupado = instance.id_lugar
        ocupado.status = True
        ocupado.save()