from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_instructor",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nombre}: {self.especialidad}"


class Alumno(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil_alumno"
    )
    legajo = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField(auto_now_add=True)


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
