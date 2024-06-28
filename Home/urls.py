from django.urls import path
from Home.views import *


urlpatterns = [
    path("", home, name="home"),
    path("amanecer/", amanecer, name="amanecer"),
    path("trail-crp/", trail_crp, name="trailcrp"),
]
