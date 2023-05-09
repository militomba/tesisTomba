from datetime import datetime
from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lugar, LugarOcupado, CentroComercialEspecifico
from django.urls import reverse
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO
from rest_framework import viewsets, status
from rest_framework.response import Response
import pyzbar.pyzbar as pyzbar
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse

def asignarLugar():
    lugarAsignado = Lugar.objects.filter(status=True).first()

    if lugarAsignado is None:
        return None
    
    lugarAsignado.status = False
    lugarAsignado.save()

    #agrego un lugar a la tabla LugarOcupado
    lugarOcupado = LugarOcupado.objects.create(lugar=lugarAsignado,   
                                               fecha = datetime.now().date(),
                                               hora_entrada = datetime.now().time()) 
                                            
    lugarOcupado.save()

    centroComercial = lugarAsignado.id_cc.nombre

    #generar codigo QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data('http://192.168.54.175:8081/liberarLugar/'+str(lugarAsignado.lugar)+'/')
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    #guardar qr
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    qr_file = InMemoryUploadedFile(buffer, None, lugarAsignado.lugar+'.png', 'img/png', buffer.getbuffer().nbytes, None)
    # lugarAsignado.codigo_qr.save(f'{lugarAsignado.lugar}.png',ContentFile(buffer.getvalue()),save=False)
    lugarAsignado.codigo_qr.save(lugarAsignado.lugar+centroComercial+'.png', qr_file, save=True)
    lugarAsignado.save()

    imagen = lugarAsignado.codigo_qr.url

    info={
        'lugar': lugarOcupado.lugar,
        'nivel':lugarAsignado.nivel,
        'fecha':lugarOcupado.fecha,
        'horario':lugarOcupado.hora_entrada,
        'centroComercial': centroComercial,
        'imagen': imagen
    }
    return info


def liberarLugar(request, lugar):
    lugarAsignado = Lugar.objects.filter(lugar=lugar).first()

    if lugarAsignado is None:
        return HttpResponse("El lugar no fue encontrado")
    lugarAsignado.status = True
    lugarAsignado.save()

    lugarOcupado = LugarOcupado.objects.filter(lugar=lugarAsignado).last()
    lugarOcupado.delete()

    lugarAsignado.codigo_qr.delete()
    context ={
        'lugar':lugarAsignado.lugar
     }
    return render(request, 'liberarLugar.html', context)
    #return HttpResponse('Lugar '+str(lugarAsignado.lugar)+' liberado exitosamente')
    

def detalleLugar(request):
    infoLugar = asignarLugar()
    
    if infoLugar:
        lugar = infoLugar['lugar']
        nivel =infoLugar['nivel']
        imagen = infoLugar['imagen']
        fecha=infoLugar['fecha']
        hora = infoLugar['horario']
        centroComercial = infoLugar['centroComercial']
        
        
        context={
            'lugar': lugar,
            'nivel':nivel,
            'fecha':fecha,
            'horario':hora,
            'imagen': imagen,
            'centroComercial': centroComercial
        }
        

        return render(request, 'detalleLugar.html', context)
    else:
        # Si no hay lugares disponibles, renderizar un template con un mensaje indicando que no hay lugares disponibles
        return render(request, 'sin_lugares.html')
    

def centroComercial(request, nombre):
    centro_comercial = CentroComercialEspecifico.objects.get(nombre__iexact=nombre)
    return render(request, 'detalle_centro_comercial.html', {'nombre': centro_comercial.nombre, 'imagen': centro_comercial.imagen.url})