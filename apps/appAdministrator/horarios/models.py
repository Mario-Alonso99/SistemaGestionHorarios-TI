from django.db import models
from apps.appDirection.teachers.models import Teacher
from apps.appDirection.asignaturas.models import Asignatura
from apps.appDirection.places.models import Place

# Create your models here.
#Creamos los datos que van a contener las Listas desplegables de forma estatica
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

class Cabecera(models.Model):
    id_usuario = models.TextField(max_length=100, verbose_name="Id_usuario", null=False, blank=False)
    fecha = models.TextField(max_length=100, verbose_name="Fecha", null=False, blank=False)
    especialidad = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_ESPECIALIDAD, default='Área Entornos Virtuales y Negocios Digitales', verbose_name="Especialidad")
    cuatrimestre = models.IntegerField(null=False, blank=False, choices=STUDENT_CHOICES_CUATRIMESTRE, default='1', verbose_name="Cuatrimestre")
    grupo = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_GRUPO, default='A', verbose_name="Grupo")
    anexos = models.TextField(max_length=100, verbose_name="Anexos", null=False, blank=False)

class Contenido(models.Model):
    cabecera = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE)
    hora = models.TextField(max_length=50, verbose_name="hora", null=False, blank=False)
    maestro_lun = models.ForeignKey(Teacher, verbose_name="Maestrolunes", on_delete=models.CASCADE, related_name="m_lunes")
    asignatura_lun = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes", on_delete=models.CASCADE, related_name="a_lunes")
    ubicacion_lun = models.ForeignKey(Place, verbose_name="Ubicaciónlunes", on_delete=models.CASCADE, related_name="u_lunes")
    maestro_mar = models.ForeignKey(Teacher, verbose_name="Maestromartes", on_delete=models.CASCADE, related_name="m_martes")
    asignatura_mar = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes", on_delete=models.CASCADE, related_name="a_martes")
    ubicacion_mar = models.ForeignKey(Place, verbose_name="Ubicaciónmartes", on_delete=models.CASCADE, related_name="u_martes")
    maestro_mie = models.ForeignKey(Teacher, verbose_name="Maestromiercoles", on_delete=models.CASCADE, related_name="m_miercoles")
    asignatura_mie = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles", on_delete=models.CASCADE, related_name="a_miercoles")
    ubicacion_mie = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles", on_delete=models.CASCADE, related_name="u_miercoles")
    maestro_jue = models.ForeignKey(Teacher, verbose_name="Maestrojueves", on_delete=models.CASCADE, related_name="m_jueves")
    asignatura_jue = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves", on_delete=models.CASCADE, related_name="a_jueves")
    ubicacion_jue = models.ForeignKey(Place, verbose_name="Ubicaciónjueves", on_delete=models.CASCADE, related_name="u_jueves")
    maestro_vie = models.ForeignKey(Teacher, verbose_name="Maestrovie", on_delete=models.CASCADE, related_name="m_viernes")
    asignatura_vie = models.ForeignKey(Asignatura, verbose_name="Asignaturavie", on_delete=models.CASCADE, related_name="a_viernes")
    ubicacion_vie = models.ForeignKey(Place, verbose_name="Ubicaciónvie", on_delete=models.CASCADE, related_name="u_viernes")