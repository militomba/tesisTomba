from django.urls import path, include
from .views import *

urlpatterns = [
        path('login/', Usuarios.user_login, name='login'),
        path('register/', Usuarios.register, name='register'),
        path('administrador/', Usuarios.administrador, name='administrador'),
        path('usuario/', Usuarios.listUsuario, name='usuario'),
        path('detalleusuario/<int:usuarioID>', Usuarios.detalleUsuario, name='detalleUsuario'),
        path('agregarCentro/<int:usuarioID>', Usuarios.agregarCentroComercial, name='agregarCentro')
    
]