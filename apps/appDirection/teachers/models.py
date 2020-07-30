from django.db import models

#Imporamos el Modelo que Utiliza Django para su Autentificación
from django.contrib.auth.models import User

#Creamos los datos que van a contener las Listas desplegables de forma Unica
TEACHER_CHOICES_TJORNADA = (
    ('AP', 'AP'),
    ('TCP', 'TCP'),
)

TEACHER_CHOICES_ESTATUS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)

#Creación del Modelo Students empleando el Modelo de User de Django
class Teacher(User):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula", null=False, blank=False)
    grado_academico = models.TextField(max_length=200, verbose_name="Grado academico", null=False, default='')
    tjornada = models.TextField(null=False, blank=False, choices=TEACHER_CHOICES_TJORNADA, default='AP')
    numero_empleado = models.TextField(max_length=200, verbose_name="Número de empleado", null=False)
    estatus = models.TextField(null=False, blank=False, choices=TEACHER_CHOICES_ESTATUS, default='Activo')
    tipo = models.TextField(null=False, blank=False, verbose_name="Tipo", max_length=20, default='Docente')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
