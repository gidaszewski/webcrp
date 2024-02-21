from django.urls import path
from Home.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"),
    path("carrera-de-la-mujer/", info_evento_actual, name="info-evento-actual"),
    path("chana-challenge/", info_chana, name="info-chana"),
    path("mantenimiento/", mantenimiento, name="mantenimiento"),
    path("sobre-nosotros/", about_us, name="sobre-nosotros"),
    path("galeria/", galery, name="galeria"),
]
