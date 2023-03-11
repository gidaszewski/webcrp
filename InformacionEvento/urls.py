from django.contrib import admin
from django.urls import path
from InformacionEvento.views import *

urlpatterns = [
    path('informacion', ChanaChallenge, name="informacion"),
]