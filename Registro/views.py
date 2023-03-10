from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *


# Create your views here.
"""class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'completado/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'"""

def Usuario_Inscripsion(request):

    if request.method == 'POST':

        primerFormulario = FormRegistro(request.POST)

        print(primerFormulario)

        if primerFormulario.is_valid():
            informacion = primerFormulario.cleaned_data
            usuario = Usuario(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                genero=informacion['genero'],
                fecha_de_nacimiento=informacion['fecha_de_nacimiento'],
                pais=informacion['pais'],
                estado=informacion['estado'],
                dni=informacion['dni'],
                telefono=informacion['telefono'],
                grupo_de_running=informacion['grupo_de_running'],
                talle_de_remera=informacion['talle_de_remera'],
                categoria=informacion['categoria'],
                email=informacion['email']
            )
            usuario.save()

    primerFormulario = FormRegistro()
    return render(request, 'Registro/registro.html', {'primerFormulario': primerFormulario})

def Completado(request):
    return render (request, 'Registro/completado.html')