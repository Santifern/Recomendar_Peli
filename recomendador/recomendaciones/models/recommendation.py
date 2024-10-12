from django.db import models
from django.contrib.auth.models import User  # Para usar el modelo de usuario predeterminado de Django
from .movie import Pelicula  # Asegúrate de que este archivo esté en el mismo módulo o carpeta


class ListaRecomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_recomendada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recomendación para {self.usuario.username}: {self.pelicula.titulo}'