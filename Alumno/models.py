from django.db import models

# Create your models here.

class Alumnos(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.EmailField(max_length=220)
    Telefono = models.IntegerField()
    imagen = models.ImageField(null=True,upload_to='img')
    
    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'
