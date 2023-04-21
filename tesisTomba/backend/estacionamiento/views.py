from django.http import HttpResponse
from django.shortcuts import render
from estacionamiento.models import *
from .serializers import *
from rest_framework import serializers, views, viewsets, status
from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import response
from rest_framework.response import Response
from codigoQR import *



class centroComercialViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CentroComercialEspecifico.objects.all()
        serializer = CentroComercialEspSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk=None):
        queryset = CentroComercialEspecifico.objects.all()
        centroComercial = get_object_or_404(queryset, centroComercial=pk)
        serializer = CentroComercialEspSerializer(centroComercial)
        return Response(serializer.data)
    
    def create(self, request):
        post_data = request.data
        serializer = CentroComercialEspCreateSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        post_data = request.data
        centroComercial = CentroComercialEspecifico.objects.get(pk=pk)
        serializer = CentroComercialEspUpdateSerializer(centroComercial, data=post_data,
                                                         partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class LugaresViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Lugares.objects.all()
        serializer = LugaresSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk=None):
        queryset = Lugares.objects.all()
        centroComercial = get_object_or_404(queryset, centroComercial=pk)
        serializer = CentroComercialEspSerializer(centroComercial)
        return Response(serializer.data)
    
    def create(self, request):
        post_data = request.data
        serializer = LugaresCreateSerializers(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        post_data = request.data
        centroComercial = Lugares.objects.get(pk=pk)
        serializer = LugaresUpdateSerializers(centroComercial, data=post_data,
                                                         partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class LugaresOcupadosViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = LugaresOcupados.objects.all()
        serializer = LugaresOcupadosSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk=None):
        queryset = LugaresOcupados.objects.all()
        centroComercial = get_object_or_404(queryset, centroComercial=pk)
        serializer = CentroComercialEspSerializer(centroComercial)
        return Response(serializer.data)
    
    def create(self, request):
        post_data = request.data
        serializer = LugaresOcupadosCreateSerializers(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    
        
    

