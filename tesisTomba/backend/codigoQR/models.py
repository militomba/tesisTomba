from django.core.files import File
from django.conf import settings
import qrcode
from qrcode import QRCode
from django.db import models
from io import BytesIO
from PIL import Image, ImageDraw


class CodigoQR(models.Model):
    name = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='qr_Code', blank=True)
    def __str__(self):
        return str(self.contenido)
    
    def save(self, *args, **kwargs):
        qrcode_img= qrcode.make(self.contenido)
        canvas = Image.new('RGB',(320,320), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        qrname = f'qr_code{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.imagen.save(qrname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
       
        

