from django.shortcuts import render
import json
import os
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "Home/home.html")


def info_evento_actual(request):
    return render(request, "Home/carrera_de_la_mujer_info.html")


def info_chana(request):
    return render(request, "Home/chana_challenge.html")


def mantenimiento(request):
    return render(request, "Home/mantenimiento.html")


def about_us(request):
    return render(request, "Home/nosotros.html")


def galery(request):
    json_path = os.path.join(settings.STATIC_ROOT, "Home", "images.json")

    with open(json_path) as f:
        images_json = json.load(f)

    context = {
        "images": images_json["images"],
    }

    return render(request, "Home/galeria.html", context)
