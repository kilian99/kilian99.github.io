from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    personas = models.IntegerField()

    def __str__(self):
        return f'Reserva de {self.nombre}'
