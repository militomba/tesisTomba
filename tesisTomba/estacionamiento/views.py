from datetime import datetime
from pyexpat.errors import messages
from django.contrib import messages
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
from django.db import IntegrityError

class CentrosComercialesViews(viewsets.ViewSet):
    def listCentroComercial(request):
        ccListados = CentroComercialEspecifico.objects.all()
        return render(request, "gestionCentrosComerciales.html", {"cc": ccListados})
    
    def detalle_centro(request, nombre):
        centro = get_object_or_404(CentroComercialEspecifico, nombre=nombre)
        return render(request, 'detalle_centro.html', {'nombre': centro.nombre,'cantLugares': centro.cantidadLugares,'niveles':centro.niveles ,'imagen': centro.imagen.url})
        #return render(request, 'detalle_centro.html', {'cc': centro})


    def crearCentroComercial(request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            cantidad_lugares = int(request.POST.get('cantidadLugares'))
            niveles = int(request.POST.get('niveles'))
            contenido = request.POST.get('contenido')
            imagen = request.FILES.get('imagen')

            try:
            # Crear el centro comercial
                centro_comercial = CentroComercialEspecifico(
                    nombre=nombre,
                    cantidadLugares=cantidad_lugares,
                    niveles=niveles,
                    contenido=contenido
                )

                if imagen:
                    centro_comercial.imagen = imagen

                # Llamar a la función para generar el código QR y guardar la imagen
                centro_comercial.crear_centro_comercial()

                # Renderizar el template con el código QR generado
                return render(request, 'crearCentroComercial.html', {'qr_code': centro_comercial.imagen.url})
            except IntegrityError: 
                error_message = 'Ya existe un centro con el mismo nombre.'
                return render( request, 'crearCentroComercial.html', {'error': error_message})

        return render(request, 'crearCentroComercial.html')
    
    def eliminarCentroComerial(request, nombre):
        centroComercial=CentroComercialEspecifico.objects.get(nombre=nombre)
        if request.method == 'POST':
            centroComercial.delete()
            return redirect('centroComercial') 
        return render(request, 'eliminarCentroComercial.html', {'centroComercial':centroComercial})

    def edicionCentroComercial(request, nombre):
        cc = CentroComercialEspecifico.objects.get(nombre=nombre)
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            cantidad_lugares = int(request.POST.get('cantidadLugares'))
            niveles = int(request.POST.get('niveles'))
            contenido = request.POST.get('contenido')
            imagen = request.FILES.get('imagen')

            cc.nombre = nombre
            cc.cantidadLugares=cantidad_lugares
            cc.niveles = niveles
            cc.contenido = contenido

            if imagen:
                cc.imagen=imagen
                
            cc.crear_centro_comercial()
            cc.save()

            return redirect('detalle_centro', nombre=nombre)
        
        return render(request, "edicionCentroCoemrcial.html", {'nombre': cc.nombre,'cantLugares': cc.cantidadLugares,'niveles':cc.niveles ,'imagen': cc.imagen.url, 'contenido':cc.contenido})
            

class Funciones(viewsets.ViewSet):
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
        infoLugar = Funciones.asignarLugar()
        
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