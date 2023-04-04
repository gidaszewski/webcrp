from django.db import models

# Create your models here.
class Cupon(models.Model):
    codigo=models.CharField(max_length=50)
    porcentaje_descuento=models.IntegerField(null=True)