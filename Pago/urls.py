from django.contrib import admin
from django.urls import path
from Pago.views import *

urlpatterns = [
    path('pagar', MetodosDePago, name="pagar"),
    path('pagar/descuento', aplicar_cupon, name="pagar-descuento"),
    path('pagar/descuento/valido', mostrar_descuento, name="pagar-descuento-valido"),
    path('pagar/super_descuento/valido', mostrar_super_descuento, name="pagar-descuento-valido-30"),
]