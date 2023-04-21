from django.shortcuts import render, get_object_or_404, redirect
from .models import CodigoQR
from .serializers import *
from rest_framework import serializers, views, viewsets, status
from qrcode import QRCode

# class CodigoQR(viewsets.ViewSet):
#     def crearCodigoQR(request):
#         qr = QRCode(version=3, box_size=20, border=2)
#         qr.add_data()
#         qr.make(fit=True)
#         img = qr.make_image(fill_color=(0,0,0), back_color=(255,255,255))
#         img.save("codigoqr.png")







        
