from django.conf import settings


from django.db import models

class CentroComercialEspecifico(models.Model):
    nombre = models.CharField(max_length=200)
    lugares = models.IntegerField(default=0)
    niveles = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)

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
    qr_code = models.CharField(max_length=200, unique=True, blank=True, null=True)
    assigned_to = models.CharField(max_length=50, blank=True, null=True)
    





    


