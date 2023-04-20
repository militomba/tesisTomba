from django import forms
from .models import CodigoQR
from qrcode import make

class CodigoQRForm(forms.ModelForm):
    class Meta:
        model = CodigoQR
        fields = ['contenido']

    def save(self, commit=True):
        instance = super().save(commit=False)
        qr = make(self.cleaned_data['contenido'])
        nombre_archivo = f"{instance.id}.png"
        qr.save(f"media/codigos_qr/{nombre_archivo}")
        instance.imagen = f"codigos_qr/{nombre_archivo}"
        if commit:
            instance.save()
        return instance