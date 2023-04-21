from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


# class CodigoQRSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = CodigoQR
#         fields = '__all__'

# class CodigoQRCreateSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = CodigoQR
#         fields = 'titulo', 'contenido', 'imagen'