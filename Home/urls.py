from django.urls import path
from Home.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "home"
urlpatterns = [
    path("", home, name="home"),
    path("carrera-de-la-mujer/", info_evento_actual, name="info-evento-actual"),
    path("mantenimiento/", mantenimiento, name="mantenimiento"),
    path("galeria/", galery, name="galeria"),
    path("nosotros/", about, name="nosotros"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
