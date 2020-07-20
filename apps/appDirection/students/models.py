from django.db import models

# Create your models here.

class student_especialidad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class student_grupo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class student_cuatrimestre(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class student_estatus(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Student(models.Model):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula", null=False, blank=False)
    nombre = models.TextField(max_length=200, verbose_name="Nombre", null=False, blank=False)
    especialidad = models.ForeignKey(student_especialidad, null=False, blank=False, on_delete=models.CASCADE)
    cuatrimestre = models.ForeignKey(student_cuatrimestre, null=False, blank=False, on_delete=models.CASCADE)
    grupo = models.ForeignKey(student_grupo, null=False, blank=False, on_delete=models.CASCADE)
    email = models.TextField(max_length=200, verbose_name="Email", null=False, blank=False)
    password = models.TextField(max_length=200, verbose_name="Contraseña", null=False, blank=False)
    estatus = models.ForeignKey(student_estatus, null=False, blank=False, on_delete=models.CASCADE)    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['cuatrimestre', 'grupo', 'especialidad']

    def __str__(self):
        return self.nombre
