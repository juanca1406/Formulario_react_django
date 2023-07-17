from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=300)