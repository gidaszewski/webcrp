from django import forms
from .models import *
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class FormRegistro(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    genero = forms.CharField(required=True)
    fecha_de_nacimiento = forms.DateField(required=True)
    pais = forms.CharField(required=True)
    estado = forms.CharField(required=True)
    dni = forms.IntegerField(required=True)
    telefono = forms.IntegerField(required=True)
    grupo_de_running = forms.CharField(required=True)
    talle_de_remera = forms.CharField(required=True)
    categoria  = forms.CharField(required=True)
    email=forms.EmailField(required=True)