from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    preferencias_generos = models.CharField(max_length=255, blank=True)  # Ej: "acción,comedia"
    
    def __str__(self):
        return self.user.username