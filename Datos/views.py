from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import EmailForm

# views.py

from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = request.POST['remitente']
        destinatario = 'juancgonzalez0901@gmail.com'
        send_mail(asunto, mensaje, remitente, [destinatario])
        return HttpResponseRedirect('/mail-enviado/')
    else:
        return render(request, 'Datos/mail.html')
    
def enviado(request):
    return render (request, 'Datos/enviado.html')
