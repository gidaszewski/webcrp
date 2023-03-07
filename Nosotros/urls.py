from django.contrib import admin
from django.urls import path
from Nosotros.views import *

urlpatterns = [
    path('nosotros/', Sobre_Nostros, name='sobre-nosotros')
]
