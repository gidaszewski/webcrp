from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Home/index.html")


def trail_crp(request):
    return render(request, "Home/trail-crp.html")


def amanecer(request):
    return render(request, "Home/amanecer.html")


def salud(request):
    return render(request, "Home/maraton-salud.html")
