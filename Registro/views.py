from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *
from django.http import FileResponse
import re
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

# Create your views here.

def descargar_pdf(request):
    file_path = '/home/fran/webcrp/staticfiles/webcrp/DESLINDE-CHANA-CHALENGE.pdf'
    file = open(file_path, 'rb')
    response = FileResponse(file, as_attachment=True, filename='DESLINDE-CHANA-CHALENGE.pdf')
    return response

def Usuario_Inscripsion(request):

    if request.method == 'POST':

        primerFormulario = FormRegistro(request.POST)

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
                distancia=informacion['distancia'],
                telefono=informacion['telefono'],
                grupo_de_running=informacion['grupo_de_running'],
                talle_de_remera=informacion['talle_de_remera'],
                categoria=informacion['categoria'],
                email=informacion['email']
            )
            emailinvalido = "este mail ya existe"
            user = Usuario.objects.all()
            valores_email = []
            for objeto in user:
                valor_email = objeto.email
                valores_email.append(valor_email)
            for i in valores_email:
                if i == usuario.email:
                    return render(request, 'Registro/registro.html', {'primerFormulario': primerFormulario, 'errors2': emailinvalido})
                else:
                    usuario.save()
                    mensaje = "¡Felicidades! Te has pre-inscripto en Chaná Challenge. Hemos notado que aún no has realizado el pago para completar tu inscripción, para pagar ingresá en www.costarioparana.com/pagar. Si no recibimos tu pago, tus datos serán eliminados de nuestra base en 72hs a partir de hoy. IMPORTANTE: Recordá subir el comprobante del pago en nuestra web para finalizar tu inscripción."
                    correo = EmailMessage(
                        'Chaná Challenge: Pre inscripción exitosa',
                        mensaje,
                        to=[informacion['email']],
                    )
                    correo.send()
                    return render(request, 'Registro/completado.html')
            return render(request, 'Registro/completado.html')

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
