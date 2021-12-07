from django.db import models
from adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    foto = models.ImageField(upload_to="fotos", null=True, blank=True )
    persona = models.ForeignKey(Persona, null=True,blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna)

    def __str__(self):
        return self.nombre