from django.db import models

# Create your models here.
class Cupon(models.Model):
    codigo=models.CharField(max_length=50)