from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class CentroComercialEspSerializer(serializers.ModelSerializer):
    class Meta():
        model = CentroComercialEspecifico
        fields = '__all__'

class CentroComercialEspCreateSerializer(serializers.ModelSerializer):
    class Meta():
        model = CentroComercialEspecifico
        fields =('nombre', 'lugares', 'niveles', 'direccion')

class CentroComercialEspUpdateSerializer(serializers.ModelSerializer):
    class Meta():
        model = CentroComercialEspecifico
        fields =('nombre')

#---------------------------------------------------------------------

class LugaresSerializer(serializers.ModelSerializer):
    class Meta():
        model = Lugares
        fields = '__all__'

class LugaresCreateSerializers(serializers.ModelSerializer):
    centroComercial = CentroComercialEspSerializer(read_only=True)
    id_cc = serializers.PrimaryKeyRelatedField(queryset = CentroComercialEspecifico.objects.all(),
    source='id_cc')

    class Meta():
        model = Lugares
        fields =('lugare', 'status','nivel', 'id_cc')
    
class LugaresUpdateSerializers(serializers.ModelSerializer):
    class Meta():
        model = Lugares
        fields =('status')

#---------------------------------------------------------------------



    