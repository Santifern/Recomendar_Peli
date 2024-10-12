import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .models import Pelicula, PerfilUsuario, Reseña

# Función para calcular la matriz de similitud entre películas
def calcular_similitud_peliculas():
    # Obtener todas las películas y sus géneros
    peliculas = Pelicula.objects.all()
    
    # Crear una lista para almacenar los géneros de cada película en formato numérico
    generos_unicos = list(set([pelicula.genero for pelicula in peliculas]))
    
    # Matriz de características de películas (una fila por cada película)
    caracteristicas_peliculas = []
    for pelicula in peliculas:
        # Convertir los géneros en una representación binaria (0 o 1)
        caracteristicas = [1 if genero in pelicula.genero else 0 for genero in generos_unicos]
        caracteristicas_peliculas.append(caracteristicas)
    
    # Convertir la lista a una matriz de numpy
    caracteristicas_peliculas = np.array(caracteristicas_peliculas)
    
    # Calcular la similitud de coseno entre las películas
    matriz_similitud = cosine_similarity(caracteristicas_peliculas)
    
    return matriz_similitud, peliculas

# Función para recomendar películas a un usuario basado en su historial de reseñas
def recomendar_peliculas(usuario):
    # Obtener la matriz de similitud de películas
    matriz_similitud, peliculas = calcular_similitud_peliculas()
    
    # Obtener las reseñas del usuario
    reseñas_usuario = Reseña.objects.filter(usuario=usuario)
    
    # Si el usuario no tiene reseñas, devolver las películas más populares (por ejemplo)
    if not reseñas_usuario.exists():
        return Pelicula.objects.order_by('-calificacion_promedio')[:5]  # 5 más populares
    
    # Crear una lista para almacenar las puntuaciones de similitud
    puntuaciones_peliculas = np.zeros(len(peliculas))
    
    # Para cada película que el usuario ha calificado, agregar la similitud con otras películas
    for reseña in reseñas_usuario:
        pelicula_indice = list(peliculas).index(reseña.pelicula)
        puntuaciones_peliculas += matriz_similitud[pelicula_indice] * reseña.calificacion
    
    # Ordenar las películas por puntuación, excluyendo las ya vistas
    peliculas_recomendadas = [
        pelicula for pelicula, puntaje in sorted(
            zip(peliculas, puntuaciones_peliculas),
            key=lambda x: x[1],
            reverse=True
        )
        if pelicula not in [r.pelicula for r in reseñas_usuario]
    ]
    
    # Devolver las 5 mejores recomendaciones
    return peliculas_recomendadas[:5]
