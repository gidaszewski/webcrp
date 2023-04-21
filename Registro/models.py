from django.db import models
from import_export import resources

# Create your models here.
tipos_categorias = [
        ("", 'Seleccione una categoria'),
        ("15-19", 'Edad: 15-19 años'),
        ("20-24", 'Edad: 20-24 años'),
        ("25-29", 'Edad: 25-29 años'),
        ("30-34", 'Edad: 30-34 años'),
        ("35-39", 'Edad: 35-39 años'),
        ("40-44", 'Edad: 40-44 años'),
        ("40-44", 'Edad: 45-49 años'),
        ("50-54", 'Edad: 50-54 años'),
        ("55-59", 'Edad: 55-59 años'),
        ("60-64", 'Edad: 60-64 años'),
        ("65-69", 'Edad: 65-69 años'),
        ("70", 'Edad: +70 años')
        ]

tipos_remeras = [
        ("", 'Seleccione un talle de remera'),
        ("XS", 'XS'),
        ("S", 'S'),
        ("M", 'M'),
        ("L", 'L'),
        ("XL", 'XL'),
	("XXL", 'XXL')
        ]

tipos_generos = [
        ("", 'Seleccione su genero'),
        ("Masculino", 'Masculino'),
        ("Femenino", 'Femenino'),
        ("Otros", 'Otros')
        ]

tipos_distancias = [
        ("", 'Seleccione una distancia'),
        ("5", '5K TREKKING'),
        ("5k", '5K COMPETITIVO'),
        ("10", '10K COMPETITIVO'),
        ("21k", '21K COMPETITIVO'),
        ]

class Usuario(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)
    genero = models.CharField(max_length=40, null=True,
            choices=tipos_generos, default="")
    fecha_de_nacimiento = models.DateField(null=True)
    pais = models.CharField(max_length=40, null=True)
    estado = models.CharField(max_length=40, null=True)
    dni = models.IntegerField(null=True)
    distancia = models.CharField(max_length=40, null=True,
            choices=tipos_distancias, default="")
    telefono = models.BigIntegerField(null=True)
    grupo_de_running = models.CharField(max_length=40, null=True)
    talle_de_remera = models.CharField(max_length=40, null=True,
            choices=tipos_remeras, default="")
    categoria  = models.CharField(max_length=40, null=True,
            choices=tipos_categorias, default="")
    email=models.EmailField()
    compro = models.BooleanField(default=False)


class UsuarioResource(resources.ModelResource):
	class Meta:
		model = Usuario
