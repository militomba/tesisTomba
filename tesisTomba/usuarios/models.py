from django.db import models
from django.conf import settings


class TipoUsuarios(models.Model):
    tipo_usuario = models.CharField(max_length=101)


class DatosUsuarios(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tipoUsuario = models.ForeignKey(TipoUsuarios, on_delete=models.CASCADE)
    
   