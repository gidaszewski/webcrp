from django import forms
from .models import *
from django.contrib.admin import widgets
from django.core.validators import validate_email

class DateInput(forms.DateInput):
    input_type = 'date'

class FormRegistro(forms.Form):
    nombre = forms.CharField(required=True) 
    apellido = forms.CharField(required=True)
    genero = forms.ChoiceField(choices=tipos_generos, required=True)
    fecha_de_nacimiento = forms.DateField(required=True)
    pais = forms.CharField(required=True)
    estado = forms.CharField(required=True)
    dni = forms.IntegerField(required=True)
    telefono = forms.IntegerField(required=True)
    grupo_de_running = forms.CharField(required=True)
    talle_de_remera = forms.ChoiceField(choices=tipos_remeras, required=True)
    categoria  = forms.ChoiceField(choices=tipos_categorias, required=True)
    email=forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError('Ingrese un correo electrónico válido')
        return email

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
    