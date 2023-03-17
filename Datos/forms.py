from django import forms
from Datos.models import *
from django.contrib.admin import widgets

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Destinatario')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

tipos_distancias = [
        ("", 'Seleccione una distancia'),
        ("1", '5K TREKKING'),
        ("2", '5K COMPETITIVO'),
        ("3", '10K COMPETITIVO'),
        ("4", '21K COMPETITIVO'),
        ]

class ArchivoForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    distancia = forms.ChoiceField(choices=tipos_distancias, required=True, initial="")
    archivo = forms.FileField(required=True)
