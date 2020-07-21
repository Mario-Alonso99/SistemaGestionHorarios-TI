from django.db import models

# Create your models here.

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

class Student(models.Model):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula", null=False, blank=False)
    nombre = models.TextField(max_length=200, verbose_name="Nombre", null=False, blank=False)
    especialidad = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_ESPECIALIDAD, default='Área Entornos Virtuales y Negocios Digitales')
    cuatrimestre = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_CUATRIMESTRE, default='1')
    grupo = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_GRUPO, default='A')
    email = models.TextField(max_length=200, verbose_name="Email", null=False, blank=False)
    password = models.TextField(max_length=200, verbose_name="Contraseña", null=False, blank=False)
    estatus = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_ESTATUS, default='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['cuatrimestre', 'grupo', 'especialidad']

    def __str__(self):
        return self.nombre
