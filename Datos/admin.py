from django.contrib import admin
from Datos.models import *

# Register your models here.

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "distancia", "archivo"]
    search_fields = ["nombre" "apellido", "distancia"]

admin.site.register(Archivo, ArchivoAdmin)
