from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from Datos.forms import *
from Datos.models import *
from Registro.models import *

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
                email=info['email'],
                archivo=info['archivo']
            )
            emailinvalido = "Este mail ya fue ingresado"
            user = Usuario.objects.all()
            valores_email = []
            for objeto in user:
                valor_email = objeto.email
                valores_email.append(valor_email)
            for i in valores_email:
                if i == archivo.email:
                    return render(request, 'Datos/informarpago.html', {'formulario': formulario, 'errors2': emailinvalido})
                else:
                    archivo.save()
                    mensaje = "Recibimos tu pago para Chaná Challenge. Ya estas inscripto de manera correcta! Falta cada vez menos para disfrutar nuestro nuevo desafío. No olvides que realizaste el 50% del pago, lo que resta de tu inscripción deberás abonarlo cuando retires tu kit."
                    correo = EmailMessage(
                        'Inscripción exitosa',
                        mensaje,
                        to=[info['email']],
                    )
                    correo.send()
                    try:
                        usuario = Usuario.objects.get(email=archivo.email)
                        usuario.compro = True
                        usuario.save()
                    except Usuario.DoesNotExist:
                        # Si el usuario no existe, puedes mostrar un mensaje de error o manejarlo de otra forma.
                        pass
                    return HttpResponseRedirect('/completado-comprobante/', {'archivo': archivo})
            return HttpResponseRedirect('/completado-comprobante/', {'archivo': archivo})
    formulario = ArchivoForm()
    return render(request, 'Datos/informarpago.html', {'formulario': formulario, 'errors': formulario.errors})

def Completado(request):
    return render (request, 'Datos/completado-comprobante.html')

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
