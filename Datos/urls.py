from django.contrib import admin
from django.urls import path
from Datos.views import *

urlpatterns = [
    path('mail/', enviar_correo, name='enviar_correo'),
    path('mail-enviado/', enviado, name='enviado')
]
