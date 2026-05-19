from django.db import models


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre}: {self.especialidad}"


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
