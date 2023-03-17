from django.db import models

# Create your models here.
tipos_distancias = [
        ("", 'Seleccione una distancia'),
        ("1", '5K TREKKING'),
        ("2", '5K COMPETITIVO'),
        ("3", '10K COMPETITIVO'),
        ("4", '21K COMPETITIVO'),
        ]

class Archivo(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)
    distancia = models.CharField(max_length=2, null=True,
            choices=tipos_distancias, default="")
    archivo = models.FileField(upload_to='infpago/infpago/media/documentos')
    fecha_subida = models.DateTimeField(auto_now_add=True)
