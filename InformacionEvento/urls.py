from django.contrib import admin
from django.urls import path
from InformacionEvento.views import *

urlpatterns = [
    path('chanachallenge', ChanaChallenge, name="chanachallenge"),
    path('maratondelasalud', MaratonDeLaSalud, name="maratondelasalud"),
]