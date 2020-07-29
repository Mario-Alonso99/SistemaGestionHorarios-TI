from django.db import models

#Imporamos el Modelo que Utiliza Django para su Autentificación
from django.contrib.auth.models import User

# Create your models here.
#Creamos los datos que van a contener las Listas desplegables de forma Unica
STUDENT_CHOICES_ESPECIALIDAD = (
    ('Área Entornos Virtuales y Negocios Digitales', 'Área Entornos Virtuales y Negocios Digitales'),
    ('Área Infraestructura de Redes Digitales', 'Área Infraestructura de Redes Digitales'),
    ('Área Desarrollo de Software Multiplataforma', 'Área Desarrollo de Software Multiplataforma'),
)

STUDENT_CHOICES_GRUPO = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),   
)

STUDENT_CHOICES_CUATRIMESTRE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'), 
    ('6', '6'), 
    ('7', '7'), 
    ('8', '8'), 
    ('9', '9'), 
    ('10', '10'),
    ('11', '11'),    
)

STUDENT_CHOICES_ESTATUS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)

#Creación del Modelo Students empleando el Modelo de User de Django
class Student(User):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula", null=False, blank=False)
    especialidad = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_ESPECIALIDAD, default='Área Entornos Virtuales y Negocios Digitales')
    cuatrimestre = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_CUATRIMESTRE, default='1')
    grupo = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_GRUPO, default='A')
    estatus = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_ESTATUS, default='Activo')
    tipo = models.TextField(null=False, blank=False, verbose_name="Tipo", max_length=20, default='Estudiante')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")