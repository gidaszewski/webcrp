from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Home/home.html")


def info_evento_actual(request):
    return render(request, "Home/carrera_de_la_mujer_info.html")


def mantenimiento(request):
    return render(request, "Home/mantenimiento.html")
