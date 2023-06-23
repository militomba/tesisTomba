from django.db import models
from qrcode import QRCode
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import uuid
from PIL import Image
from django.core.exceptions import ValidationError
import jwt



class CentroComercialEspecifico(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    cantidadLugares = models.IntegerField(default=0)
    niveles = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='qr_Code', blank=True, null=True)
    # contenido = models.CharField(max_length=200)

    def __str__(self):
        return(self.nombre)
    
   
    def crear_centro_comercial(self, *args, **kwargs):
        self.nombre = self.nombre.upper()

        archivojwt = {
            'centroComercial':self.nombre,
        }
        token = jwt.encode(archivojwt, '1234', algorithm='HS256')
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data('https://192.168.54.175:8081/funcion/detalleLugarAsignado/'+self.nombre+'/?token=' + token)
        qr.make(fit=True)
        # Generar la imagen del código QR
        img = qr.make_image(fill='black', back_color='white')
        # Guardar la imagen en el campo correspondiente del modelo
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.imagen.save(f'{self.nombre}.png', ContentFile(buffer.getvalue()), save=False) 
        #save=False --> para evitar que llame recursivamente al metodo save y no crear un bucle infinito
        buffer.close()
        # Llamar al método save() del modelo base
        super().save(*args, **kwargs)

    
    # def save(self,*args, **kwargs):
    #     self.nombre = self.nombre.upper()
    #     super().save(*args, **kwargs)
class Lugar(models.Model):
    lugar = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    nivel =  models.IntegerField(default=0)
    id_cc = models.ForeignKey(CentroComercialEspecifico, on_delete=models.CASCADE, null=False, related_name='lugares_cc')
    codigo_qr = models.ImageField(upload_to='qr_code', null=True, blank=True)

    def __str__(self):
        lugar = self.lugar
        cc = self.id_cc.nombre
        status = self.status
        return (cc + " - Lugar: "+ lugar +" - Status: " + str(status))
    
    


class LugarOcupado(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    hora_entrada = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return("Lugar: " + self.lugar.lugar + " - "+
               self.lugar.id_cc.nombre)