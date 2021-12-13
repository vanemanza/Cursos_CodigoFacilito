from django.db import models

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField() 
    telefono = models.CharField(max_length=12)
    email = models.EmailField()  
    domicilio = models.TextField()  

    def __str__(self):
        return f'{self.nombre} {self.apellido}'