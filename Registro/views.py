from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *
from django.http import FileResponse


# Create your views here.
def descargar_pdf(request):
    file_path = 'C:/Users/juanc/Desktop/webcrp/Registro/static/webcrp/DESLINDE-CHANA-CHALENGE.pdf'
    file = open(file_path, 'rb')
    response = FileResponse(file, as_attachment=True, filename='DESLINDE-CHANA-CHALENGE.pdf')
    return response


class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'completado/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'

def Completado(request):
    return render (request, 'Registro/completado.html')