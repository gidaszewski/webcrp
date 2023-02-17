from django import forms
from .models import *
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class FormRegistro(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    genero = forms.CharField()
    fecha_de_nacimiento = forms.DateField()
    pais = forms.CharField()
    estado = forms.CharField()
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    grupo_de_running = forms.CharField()
    talle_de_remera = forms.CharField()
    categoria  = forms.CharField()
    email=forms.EmailField()
    class Meta:
        widgets= {'fecha_de_nacimiento': DateInput()}
    