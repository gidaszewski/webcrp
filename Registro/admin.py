from django.contrib import admin
from Registro.models import *

# Register your models here.
admin.site.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fields = ('nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria')
    list_display_links = ('nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria')
    list_display = ('nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria')
    list_editable = ('nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria')
    search_fields = ['code', 'name']
    list_per_page = 15