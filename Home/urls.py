from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path("", home, name="home"),
    path("carrera-de-la-mujer/", info_evento_actual, name="info-evento-actual"),
    path("mantenimiento/", mantenimiento, name="mantenimiento"),
]
