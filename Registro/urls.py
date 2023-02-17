from django.contrib import admin
from django.urls import path
from Registro.views import *

urlpatterns = [
    path('registro/', Usuario_Inscripsion.as_view(), name="registro"),
]
