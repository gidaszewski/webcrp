from django.urls import path
from Home.views import *


urlpatterns = [
    path("", home, name="home"),
    path("trail-crp/", trail_crp, name="trailcrp"),
    path("amanecer/", amanecer, name="amanecer"),
    path("maraton-salud/", salud, name="salud"),
]
