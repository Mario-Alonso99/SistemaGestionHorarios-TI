from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


ASIGNATURAS_CHOICES_ESPECIALIDAD = (
    ('Área Entornos Virtuales y Negocios Digitales', 'Área Entornos Virtuales y Negocios Digitales'),
    ('Área Infraestructura de Redes Digitales', 'Área Infraestructura de Redes Digitales'),
    ('Área Desarrollo de Software Multiplataforma', 'Área Desarrollo de Software Multiplataforma'),
)

ASIGNATURAS_CHOICES_CUATRIMESTRE = (
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

class Asignatura(models.Model):
    nombre = models.TextField(max_length=200, verbose_name="Nombre", null=False, blank=False)
    especialidad = models.TextField(null=False, blank=False, choices=ASIGNATURAS_CHOICES_ESPECIALIDAD, default='Área Entornos Virtuales y Negocios Digitales')
    cuatrimestre = models.TextField(null=False, blank=False, choices=ASIGNATURAS_CHOICES_CUATRIMESTRE, default='1')
    

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['especialidad', 'cuatrimestre']

    def __str__(self):
        return self.nombre