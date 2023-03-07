from django.shortcuts import render

# Create your views here.
def Sobre_Nostros(request):
    return render(request, 'Nosotros/Sobre_Nosotros.html')