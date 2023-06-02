from django.urls import path, include
from .views import *

urlpatterns = [
        path('login/', Usuarios.user_login, name='login'),
        path('register/', Usuarios.register, name='register'),
        path('administrador/', Usuarios.administrador, name='administrador'),

    
]