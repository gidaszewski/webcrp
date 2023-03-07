from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *


# Create your views here.
class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'registro/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'

