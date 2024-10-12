from django.db import models


# Creation movies table and fields 

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=100)
    sinopsis = models.TextField()
    duracion = models.IntegerField()  # En minutos
    idioma = models.CharField(max_length=50)
    calificacion_promedio = models.FloatField(default=0)
    
    def __str__(self):
        return self.titulo