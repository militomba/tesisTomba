from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from estacionamiento.models import *
from django.contrib.auth.models import User






class Usuarios(viewsets.ViewSet):
    def register(request):
        if request.method == 'POST':
            username = request.POST['usuario']
            password = request.POST['password']
            email = request.POST['email']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            tipoUsuario = request.POST['tipo_usuario']
            # Crear un nuevo usuario en la base de datos
            
            
            tipo_usuario = TipoUsuarios.objects.get(id=tipoUsuario)
            # Crear una instancia de DatosUsuarios relacionada con el nuevo usuario
            datos_usuario = DatosUsuarios(usuario=username, nombre=nombre, apellido=apellido, email=email, password=password, tipoUsuario=tipo_usuario)
            datos_usuario.save()
            return redirect('login')
        
        tipoUsuarios = TipoUsuarios.objects.all()
        return render(request, 'register.html', {'tipoUsuario': tipoUsuarios})

    def user_login(request):
        if request.method == 'POST':
            username = request.POST['usuario']
            password = request.POST['password']
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
            # Iniciar sesión
                login(request, user)
                datos_usuario = DatosUsuarios.objects.get(usuario=username)
                tipo_usuario = datos_usuario.tipoUsuario.tipo_usuario
                if tipo_usuario == 'Administrador':
                    return redirect('administrador')  # Redirigir a la página del administrador
                elif tipo_usuario == 'Centro Comercial':
                    return redirect('estacionamiento:listLugares', datos_usuario.centroComercial.nombre)  # Redirigir a la página del centro comercial
                elif tipo_usuario == 'Scanner QR':
                    return redirect('ruta_scanner_qr')  # Redirigir a la página del scanner QR # Redirigir a la página de inicio
            else:
                # Usuario no válido
                return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
        return render(request, 'login.html')

    def user_logout(request):
        logout(request)
        return redirect('login')
    

    #ADMINISTRADOR
    def administrador(request):
        return render(request, 'admin.html')
    
    def listUsuario(request):
        usuario = DatosUsuarios.objects.all()
        
        return render(request, 'usuario.html', {'usuario':usuario})
    
    def detalleUsuario(request, usuarioID):
        usuario = get_object_or_404(DatosUsuarios, id=usuarioID)
        cc_vacio=False
        if not usuario.centroComercial:
            cc_vacio=True
        return render (request, 'detalleUsuario.html', {'usuario':usuario, 'cc_vacio':cc_vacio})

    def agregarCentroComercial(request, usuarioID):
        cc = CentroComercialEspecifico.objects.all()
        usuario = get_object_or_404(DatosUsuarios, id=usuarioID)
        
        if request.method == 'POST':
            centroComercial = request.POST.get('centroComercial')
            centro = get_object_or_404(CentroComercialEspecifico, id=centroComercial)
            
            usuario.centroComercial = centro
            usuario.save()
            return redirect('detalleUsuario', usuarioID)
        
        return render(request, 'agregarCentroComercial.html', {'cc': cc, 'usuario': usuario})


    #USUARIOS CENTROS COMERCIALES
        
    
    


