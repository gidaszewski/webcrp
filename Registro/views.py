from django.shortcuts import render
from Registro.forms import *
from Registro.models import *

# Create your views here.
def formRegistro(request):

    if request.method == 'POST':

        primerFormulario = FormRegistro(request.POST)

        print(primerFormulario)

        if primerFormulario.is_valid:

            informacion = primerFormulario.cleaned_data

            email = Usuario(email=informacion['email'])

            email.save()

            return render(request, 'Registro/datos.html')
    else:

        primerFormulario = FormRegistro()

    return render(request, 'Registro/registro.html', {'primerFormulario': primerFormulario})