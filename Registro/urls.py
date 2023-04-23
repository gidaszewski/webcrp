from django.contrib import admin
from django.urls import path
from Registro.views import *


urlpatterns = [
    path('registro_soldout/', Usuario_Inscripsion, name="registro"),
    path('completado/', Completado, name="completado"),
    path('descargar-pdf/', descargar_pdf, name="descargar_pdf"),
]
