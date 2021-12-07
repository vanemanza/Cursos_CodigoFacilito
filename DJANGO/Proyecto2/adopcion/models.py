from django.db import models

# Create your models here.
class Persona(models.Model):
    
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    info = models.TextField()    
    

    def __str__(self):
        return self.nombre
