from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from Datos.forms import *
from Datos.models import *

# views.py

from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = request.POST['remitente']
        destinatario = 'info@costarioparana.com.ar'
        send_mail(asunto, mensaje, remitente, [destinatario])
        return HttpResponseRedirect('/mail-enviado/')
    else:
        return render(request, 'Datos/mail.html')
    
def enviado(request):
    return render (request, 'Datos/enviado.html')

def cargar_archivo(request):
    if request.method == 'POST':
        formulario = ArchivoForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            archivo = Archivo(
                nombre=info['nombre'],
                apellido=info['apellido'],
                distancia=info['distancia'],
                archivo=info['archivo']
            )
            archivo.save()
            return render(request, 'Datos/completado.html', {'archivo': archivo})
    formulario = ArchivoForm()
    return render(request, 'Datos/informarpago.html', {'formulario': formulario, 'errors': formulario.errors})

def Completado(request):
    return render (request, 'Datos/completado.html')
