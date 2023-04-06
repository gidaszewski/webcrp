from django.db import models
from import_export import resources

# Create your models here.
tipos_categorias = [
        ("", 'Seleccione una categoria'),
        ("1", 'Edad: 15-20 años'),
        ("2", 'Edad: 20-25 años'),
        ("3", 'Edad: 25-30 años'),
        ("4", 'Edad: 30-35 años'),
        ("5", 'Edad: 35-40 años'),
        ("6", 'Edad: 40-45 años'),
        ("7", 'Edad: 45-50 años'),
        ("8", 'Edad: 50-55 años'),
        ("9", 'Edad: 55-60 años'),
        ("10", 'Edad: 60-65 años'),
        ("11", 'Edad: +70 años')
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
        ("1", '5K TREKKING'),
        ("2", '5K COMPETITIVO'),
        ("3", '10K COMPETITIVO'),
        ("4", '21K COMPETITIVO'),
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
