from django.db import models

# Create your models here.
class Student(models.Model):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula")
    nombre = models.TextField(max_length=200, verbose_name="Nombre")
    especialidad = models.TextField(max_length=200, verbose_name="Especialidad")
    cuatrimestre = models.TextField(max_length=20, verbose_name="Cuatrimestre")
    grupo = models.TextField(max_length=5, verbose_name="Grupo")
    email = models.TextField(max_length=200, verbose_name="Email")
    password = models.TextField(max_length=200, verbose_name="Contraseña")
    estatus = models.TextField(max_length=200, verbose_name="Estatus")    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['cuatrimestre', 'grupo', 'especialidad']

    def __str__(self):
        return self.nombre
