from django.db import models

# Create your models here.
class Vuelo(models.Model):
    num_vuelo = models.CharField(max_length=100)
    origen = models.TextField()
    destino = models.TextField()
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()
    
    def __str__(self):
        return self.num_vuelo