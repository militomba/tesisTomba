from django.shortcuts import render
from .forms import CodigoQRForm
from rest_framework import serializers, views, viewsets, status

class codigoQR(viewsets.ViewSet):
    def crear_codigo_qr(request):
        if request.method == 'POST':
            form = CodigoQRForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = CodigoQRForm()
        return render(request, 'crear_codigo_qr.html', {'form': form})
