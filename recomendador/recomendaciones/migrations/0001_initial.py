# Generated by Django 5.1.1 on 2024-10-04 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('fecha_estreno', models.DateField()),
                ('genero', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
                ('duracion', models.IntegerField()),
                ('idioma', models.CharField(max_length=50)),
                ('calificacion_promedio', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ListaRecomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recomendada', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialRecomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vista', models.BooleanField(default=False)),
                ('fecha_recomendada', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, null=True)),
                ('calificacion', models.IntegerField()),
                ('fecha_reseña', models.DateTimeField(auto_now_add=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('preferencias_generos', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
