from django.conf import settings

from django.db import models

class CodigoQR(models.Model):
    contenido = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='codigos_qr/')
