from django.contrib import admin
from django.urls import path
from Registro.views import *

urlpatterns = [
    path('registro', formRegistro, name="registro"),
]
