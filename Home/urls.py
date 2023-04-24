from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path('', home, name="home"),
    path('listado/', listado, name="listado"),
]