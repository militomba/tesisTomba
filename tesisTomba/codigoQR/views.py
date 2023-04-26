from django.shortcuts import render, get_object_or_404, redirect
from .models import CodigoQR

from rest_framework import serializers, views, viewsets, status
from qrcode import QRCode
from django.http import HttpResponse
from estacionamiento.models import *
#agregar funcion que al leer un codigo qr me muestre por pantalla el qr generado,etc

#agregar una funcion que el contenido de mi codigo qr tenga cambiar el status del lugar ocupado


def index(request):
    # Obtener el primer objeto disponible de la base de datos
    
    codigoqr = CodigoQR.objects.filter(available=True).first()
    lugarAsignado = LugaresOcupados.objects.filter(available=True).first()
    fecha = lugarAsignado.fecha
    hora_entrada = lugarAsignado.hora_entrada
    centroComercial = lugarAsignado.id_lugar.id_cc
    
    # Generar el código QR para el objeto obtenido
    codigoqr.save()
    lugarAsignado.save()
    
    # Renderizar el template y pasarle el objeto y su código QR como contexto
    context = {
        'codigoqr': codigoqr,
        'lugarAsignado': lugarAsignado,
        'fecha': fecha,
        'hora_entrada': hora_entrada,
        'centroComercial': centroComercial
     
        }
    
    return render(request, template_name='index.html', context=context)
