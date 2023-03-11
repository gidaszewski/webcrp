from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *
from django.http import FileResponse
import re

# Create your views here.

def descargar_pdf(request):
    file_path = 'C:/Users/juanc/Desktop/webcrp/Registro/static/webcrp/DESLINDE-CHANA-CHALENGE.pdf'
    file = open(file_path, 'rb')
    response = FileResponse(file, as_attachment=True, filename='DESLINDE-CHANA-CHALENGE.pdf')
    return response


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
    return render(request, 'Registro/registro.html', {'primerFormulario': primerFormulario, 'errors': primerFormulario.errors})

def Completado(request):
    return render (request, 'Registro/completado.html')

def is_valid_email(email):
    # Verificar que el correo electrónico contenga un símbolo "@"
    if "@" not in email:
        return False
    
    # Dividir el correo electrónico en nombre de usuario y dominio
    username, domain = email.split("@")
    
    # Verificar que el nombre de usuario solo contenga caracteres alfanuméricos, guiones bajos y puntos
    if not re.match(r'^[\w\.\-]+$', username):
        return False
    
    # Verificar que el dominio tenga al menos un punto y no comience ni termine con un guion
    if not re.match(r'^[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+$', domain):
        return False
    
    # Verificar que la extensión de dominio sea válida
    if not re.match(r'\.[a-zA-Z]{2,}$', domain):
        return False
    
    return True