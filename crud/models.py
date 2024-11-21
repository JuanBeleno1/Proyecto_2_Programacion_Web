from django.db import models

# Create your models here.
class Tenis(models.Model):

    nombre = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    color = models.CharField(max_length = 50)
    año_lanzamiento = models.IntegerField() 
    imagen = models.FileField(upload_to="tenis/")


    def __str__(self):
        return self.nombre

