from django.contrib import admin
from django.urls import path
from Datos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mail/', enviar_correo, name='enviar_correo'),
    path('mail-enviado/', enviado, name='enviado'),
    path('informarpago/', cargar_archivo, name="informar-pago"),
    path('completado/', Completado, name="completado"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
