from django.core.files import File
from django.conf import settings
import qrcode
from qrcode import QRCode
from django.db import models
from io import BytesIO
from PIL import Image, ImageDraw
from estacionamiento.models import *
from django.core.files.base import ContentFile

class CodigoQRCentroComercial(models.Model):
    name = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='qr_Code', blank=True, null=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
         # Generar el contenido del código QR
        contenido = self.contenido
         # Crear el código QR
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(contenido)
        qr.make(fit=True)
        # Generar la imagen del código QR
        img = qr.make_image(fill='black', back_color='white')
        # Guardar la imagen en el campo correspondiente del modelo
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.imagen.save(f'{self.name}.png', ContentFile(buffer.getvalue()), save=False) 
        #save=False --> para evitar que llame recursivamente al metodo save y no crear un bucle infinito
        buffer.close()
        # Llamar al método save() del modelo base
        super().save(*args, **kwargs)


class CodigoQR(models.Model):
    name = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='qr_Code', blank=True)
    lugar = models.ForeignKey
    available = models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
         # Generar el contenido del código QR
        contenido = self.contenido
         # Crear el código QR
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(contenido)
        qr.make(fit=True)
        # Generar la imagen del código QR
        img = qr.make_image(fill='black', back_color='white')
        # Guardar la imagen en el campo correspondiente del modelo
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.imagen.save(f'{self.name}.png', ContentFile(buffer.getvalue()), save=False) 
        #save=False --> para evitar que llame recursivamente al metodo save y no crear un bucle infinito
        buffer.close()
        # Llamar al método save() del modelo base
        super().save(*args, **kwargs)
       
