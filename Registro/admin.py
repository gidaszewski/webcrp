from django.contrib import admin
from Registro.models import *
from .models import *
from .forms import *
from import_export.admin import ExportActionMixin

# Register your models here.

class UsuarioAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = UsuarioResource
    list_display = ["nombre", "apellido", "fecha_de_nacimiento", "dni","distancia", "pais", "estado", "genero", "telefono", "talle_de_remera","categoria","email"]
    list_editable = ["talle_de_remera", "telefono", "email", "distancia"]
    search_fields = ["nombre" "apellido", "dni", "talle_de_remera",]


admin.site.register(Usuario, UsuarioAdmin)
