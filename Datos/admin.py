from django.contrib import admin
from Datos.models import *
from import_export.admin import ExportActionMixin

# Register your models here.

class ArchivoAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ArchivoResource
    list_display = ["nombre", "apellido", "distancia", "email", "archivo"]
    search_fields = ["nombre", "apellido", "distancia", "email"]
    list_editable = ["email"]

admin.site.register(Archivo, ArchivoAdmin)
