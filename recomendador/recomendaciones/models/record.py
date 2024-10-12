from django.db import models
from django.contrib.auth.models import User  # Para usar el modelo de usuario predeterminado de Django
from .movie import Pelicula  # Asegúrate de que este archivo esté en el mismo módulo o carpeta


class HistorialRecomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    vista = models.BooleanField(default=False)
    fecha_recomendada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recomendación a {self.usuario.username} - {self.pelicula.titulo}'