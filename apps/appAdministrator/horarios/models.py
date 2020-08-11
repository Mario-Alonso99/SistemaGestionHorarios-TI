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
    cuatrimestre = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_CUATRIMESTRE, default='1', verbose_name="Cuatrimestre")
    grupo = models.TextField(null=False, blank=False, choices=STUDENT_CHOICES_GRUPO, default='A', verbose_name="Grupo")
    anexos = models.TextField(max_length=100, verbose_name="Anexos", null=False, blank=False)

class Contenido(models.Model):
    cabecera1 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_1")
    hora1 = models.TextField(max_length=50, verbose_name="hora1", null=True, blank=True, default='')
    maestro_lun1 = models.ForeignKey(Teacher, verbose_name="Maestrolunes1", on_delete=models.CASCADE, related_name="m_lunes1", null=True, blank=True, default='')
    asignatura_lun1 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes1", on_delete=models.CASCADE, related_name="a_lunes1", null=True, blank=True, default='')
    ubicacion_lun1 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes1", on_delete=models.CASCADE, related_name="u_lunes1", null=True, blank=True, default='')
    maestro_mar1 = models.ForeignKey(Teacher, verbose_name="Maestromartes1", on_delete=models.CASCADE, related_name="m_martes1", null=True, blank=True, default='')
    asignatura_mar1 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes1", on_delete=models.CASCADE, related_name="a_martes1", null=True, blank=True, default='')
    ubicacion_mar1 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes1", on_delete=models.CASCADE, related_name="u_martes1", null=True, blank=True, default='')
    maestro_mie1 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles1", on_delete=models.CASCADE, related_name="m_miercoles1", null=True, blank=True, default='')
    asignatura_mie1 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles1", on_delete=models.CASCADE, related_name="a_miercoles1", null=True, blank=True, default='')
    ubicacion_mie1 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles1", on_delete=models.CASCADE, related_name="u_miercoles1", null=True, blank=True, default='')
    maestro_jue1 = models.ForeignKey(Teacher, verbose_name="Maestrojueves1", on_delete=models.CASCADE, related_name="m_jueves1", null=True, blank=True, default='')
    asignatura_jue1 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves1", on_delete=models.CASCADE, related_name="a_jueves1", null=True, blank=True, default='')
    ubicacion_jue1 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves1", on_delete=models.CASCADE, related_name="u_jueves1", null=True, blank=True, default='')
    maestro_vie1 = models.ForeignKey(Teacher, verbose_name="Maestrovie1", on_delete=models.CASCADE, related_name="m_viernes1", null=True, blank=True, default='')
    asignatura_vie1 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie1", on_delete=models.CASCADE, related_name="a_viernes1", null=True, blank=True, default='')
    ubicacion_vie1 = models.ForeignKey(Place, verbose_name="Ubicaciónvie1", on_delete=models.CASCADE, related_name="u_viernes1", null=True, blank=True, default='')

    cabecera2 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_2")
    hora2 = models.TextField(max_length=50, verbose_name="hora2", null=True, blank=True, default='')
    maestro_lun2 = models.ForeignKey(Teacher, verbose_name="Maestrolunes2", on_delete=models.CASCADE, related_name="m_lunes2", null=True, blank=True, default='')
    asignatura_lun2 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes2", on_delete=models.CASCADE, related_name="a_lunes2", null=True, blank=True, default='')
    ubicacion_lun2 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes2", on_delete=models.CASCADE, related_name="u_lunes2", null=True, blank=True, default='')
    maestro_mar2 = models.ForeignKey(Teacher, verbose_name="Maestromartes2", on_delete=models.CASCADE, related_name="m_martes2", null=True, blank=True, default='')
    asignatura_mar2 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes2", on_delete=models.CASCADE, related_name="a_martes2", null=True, blank=True, default='')
    ubicacion_mar2 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes2", on_delete=models.CASCADE, related_name="u_martes2", null=True, blank=True, default='')
    maestro_mie2 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles2", on_delete=models.CASCADE, related_name="m_miercoles2", null=True, blank=True, default='')
    asignatura_mie2 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles2", on_delete=models.CASCADE, related_name="a_miercoles2", null=True, blank=True, default='')
    ubicacion_mie2 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles2", on_delete=models.CASCADE, related_name="u_miercoles2", null=True, blank=True, default='')
    maestro_jue2 = models.ForeignKey(Teacher, verbose_name="Maestrojueves2", on_delete=models.CASCADE, related_name="m_jueves2", null=True, blank=True, default='')
    asignatura_jue2 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves2", on_delete=models.CASCADE, related_name="a_jueves2", null=True, blank=True, default='')
    ubicacion_jue2 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves2", on_delete=models.CASCADE, related_name="u_jueves2", null=True, blank=True, default='')
    maestro_vie2 = models.ForeignKey(Teacher, verbose_name="Maestrovie2", on_delete=models.CASCADE, related_name="m_viernes2", null=True, blank=True, default='')
    asignatura_vie2 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie2", on_delete=models.CASCADE, related_name="a_viernes2", null=True, blank=True, default='')
    ubicacion_vie2 = models.ForeignKey(Place, verbose_name="Ubicaciónvie2", on_delete=models.CASCADE, related_name="u_viernes2", null=True, blank=True, default='')

    cabecera3 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_3")
    hora3 = models.TextField(max_length=50, verbose_name="hora3", null=True, blank=True, default='')
    maestro_lun3 = models.ForeignKey(Teacher, verbose_name="Maestrolunes3", on_delete=models.CASCADE, related_name="m_lunes3", null=True, blank=True, default='')
    asignatura_lun3 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes3", on_delete=models.CASCADE, related_name="a_lunes3", null=True, blank=True, default='')
    ubicacion_lun3 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes3", on_delete=models.CASCADE, related_name="u_lunes3", null=True, blank=True, default='')
    maestro_mar3 = models.ForeignKey(Teacher, verbose_name="Maestromartes3", on_delete=models.CASCADE, related_name="m_martes3", null=True, blank=True, default='')
    asignatura_mar3 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes3", on_delete=models.CASCADE, related_name="a_martes3", null=True, blank=True, default='')
    ubicacion_mar3 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes3", on_delete=models.CASCADE, related_name="u_martes3", null=True, blank=True, default='')
    maestro_mie3 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles3", on_delete=models.CASCADE, related_name="m_miercoles3", null=True, blank=True, default='')
    asignatura_mie3 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles3", on_delete=models.CASCADE, related_name="a_miercoles3", null=True, blank=True, default='')
    ubicacion_mie3 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles3", on_delete=models.CASCADE, related_name="u_miercoles3", null=True, blank=True, default='')
    maestro_jue3 = models.ForeignKey(Teacher, verbose_name="Maestrojueves3", on_delete=models.CASCADE, related_name="m_jueves3", null=True, blank=True, default='')
    asignatura_jue3 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves3", on_delete=models.CASCADE, related_name="a_jueves3", null=True, blank=True, default='')
    ubicacion_jue3 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves3", on_delete=models.CASCADE, related_name="u_jueves3", null=True, blank=True, default='')
    maestro_vie3 = models.ForeignKey(Teacher, verbose_name="Maestrovie3", on_delete=models.CASCADE, related_name="m_viernes3", null=True, blank=True, default='')
    asignatura_vie3 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie3", on_delete=models.CASCADE, related_name="a_viernes3", null=True, blank=True, default='')
    ubicacion_vie3 = models.ForeignKey(Place, verbose_name="Ubicaciónvie3", on_delete=models.CASCADE, related_name="u_viernes3", null=True, blank=True, default='')
    

class SecondContenido(models.Model):
    cabecera4 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_4")
    hora4 = models.TextField(max_length=50, verbose_name="hora4", null=True, blank=True, default='')
    maestro_lun4 = models.ForeignKey(Teacher, verbose_name="Maestrolunes4", on_delete=models.CASCADE, related_name="m_lunes4", null=True, blank=True, default='')
    asignatura_lun4 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes4", on_delete=models.CASCADE, related_name="a_lunes4", null=True, blank=True, default='')
    ubicacion_lun4 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes4", on_delete=models.CASCADE, related_name="u_lunes4", null=True, blank=True, default='')
    maestro_mar4 = models.ForeignKey(Teacher, verbose_name="Maestromartes4", on_delete=models.CASCADE, related_name="m_martes4", null=True, blank=True, default='')
    asignatura_mar4 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes4", on_delete=models.CASCADE, related_name="a_martes4", null=True, blank=True, default='')
    ubicacion_mar4 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes4", on_delete=models.CASCADE, related_name="u_martes4", null=True, blank=True, default='')
    maestro_mie4 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles4", on_delete=models.CASCADE, related_name="m_miercoles4", null=True, blank=True, default='')
    asignatura_mie4 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles4", on_delete=models.CASCADE, related_name="a_miercoles4", null=True, blank=True, default='')
    ubicacion_mie4 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles4", on_delete=models.CASCADE, related_name="u_miercoles4", null=True, blank=True, default='')
    maestro_jue4 = models.ForeignKey(Teacher, verbose_name="Maestrojueves4", on_delete=models.CASCADE, related_name="m_jueves4", null=True, blank=True, default='')
    asignatura_jue4 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves4", on_delete=models.CASCADE, related_name="a_jueves4", null=True, blank=True, default='')
    ubicacion_jue4 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves4", on_delete=models.CASCADE, related_name="u_jueves4", null=True, blank=True, default='')
    maestro_vie4 = models.ForeignKey(Teacher, verbose_name="Maestrovie4", on_delete=models.CASCADE, related_name="m_viernes4", null=True, blank=True, default='')
    asignatura_vie4 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie4", on_delete=models.CASCADE, related_name="a_viernes4", null=True, blank=True, default='')
    ubicacion_vie4 = models.ForeignKey(Place, verbose_name="Ubicaciónvie4", on_delete=models.CASCADE, related_name="u_viernes4", null=True, blank=True, default='')
    
    cabecera5 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_5")
    hora5 = models.TextField(max_length=50, verbose_name="hora5", null=True, blank=True, default='')
    maestro_lun5 = models.ForeignKey(Teacher, verbose_name="Maestrolunes5", on_delete=models.CASCADE, related_name="m_lunes5", null=True, blank=True, default='')
    asignatura_lun5 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes5", on_delete=models.CASCADE, related_name="a_lunes5", null=True, blank=True, default='')
    ubicacion_lun5 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes5", on_delete=models.CASCADE, related_name="u_lunes5", null=True, blank=True, default='')
    maestro_mar5 = models.ForeignKey(Teacher, verbose_name="Maestromartes5", on_delete=models.CASCADE, related_name="m_martes5", null=True, blank=True, default='')
    asignatura_mar5 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes5", on_delete=models.CASCADE, related_name="a_martes5", null=True, blank=True, default='')
    ubicacion_mar5 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes5", on_delete=models.CASCADE, related_name="u_martes5", null=True, blank=True, default='')
    maestro_mie5 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles5", on_delete=models.CASCADE, related_name="m_miercoles5", null=True, blank=True, default='')
    asignatura_mie5 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles5", on_delete=models.CASCADE, related_name="a_miercoles5", null=True, blank=True, default='')
    ubicacion_mie5 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles5", on_delete=models.CASCADE, related_name="u_miercoles5", null=True, blank=True, default='')
    maestro_jue5 = models.ForeignKey(Teacher, verbose_name="Maestrojueves5", on_delete=models.CASCADE, related_name="m_jueves5", null=True, blank=True, default='')
    asignatura_jue5 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves5", on_delete=models.CASCADE, related_name="a_jueves5", null=True, blank=True, default='')
    ubicacion_jue5 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves5", on_delete=models.CASCADE, related_name="u_jueves5", null=True, blank=True, default='')
    maestro_vie5 = models.ForeignKey(Teacher, verbose_name="Maestrovie5", on_delete=models.CASCADE, related_name="m_viernes5", null=True, blank=True, default='')
    asignatura_vie5 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie5", on_delete=models.CASCADE, related_name="a_viernes5", null=True, blank=True, default='')
    ubicacion_vie5 = models.ForeignKey(Place, verbose_name="Ubicaciónvie5", on_delete=models.CASCADE, related_name="u_viernes5", null=True, blank=True, default='')
    
    cabecera6 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_6")
    hora6 = models.TextField(max_length=50, verbose_name="hora6", null=True, blank=True, default='')
    maestro_lun6 = models.ForeignKey(Teacher, verbose_name="Maestrolunes6", on_delete=models.CASCADE, related_name="m_lunes6", null=True, blank=True, default='')
    asignatura_lun6 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes6", on_delete=models.CASCADE, related_name="a_lunes6", null=True, blank=True, default='')
    ubicacion_lun6 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes6", on_delete=models.CASCADE, related_name="u_lunes6", null=True, blank=True, default='')
    maestro_mar6 = models.ForeignKey(Teacher, verbose_name="Maestromartes6", on_delete=models.CASCADE, related_name="m_martes6", null=True, blank=True, default='')
    asignatura_mar6 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes6", on_delete=models.CASCADE, related_name="a_martes6", null=True, blank=True, default='')
    ubicacion_mar6 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes6", on_delete=models.CASCADE, related_name="u_martes6", null=True, blank=True, default='')
    maestro_mie6 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles6", on_delete=models.CASCADE, related_name="m_miercoles6", null=True, blank=True, default='')
    asignatura_mie6 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles6", on_delete=models.CASCADE, related_name="a_miercoles6", null=True, blank=True, default='')
    ubicacion_mie6 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles6", on_delete=models.CASCADE, related_name="u_miercoles6", null=True, blank=True, default='')
    maestro_jue6 = models.ForeignKey(Teacher, verbose_name="Maestrojueves6", on_delete=models.CASCADE, related_name="m_jueves6", null=True, blank=True, default='')
    asignatura_jue6 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves6", on_delete=models.CASCADE, related_name="a_jueves6", null=True, blank=True, default='')
    ubicacion_jue6 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves6", on_delete=models.CASCADE, related_name="u_jueves6", null=True, blank=True, default='')
    maestro_vie6 = models.ForeignKey(Teacher, verbose_name="Maestrovie6", on_delete=models.CASCADE, related_name="m_viernes6", null=True, blank=True, default='')
    asignatura_vie6 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie6", on_delete=models.CASCADE, related_name="a_viernes6", null=True, blank=True, default='')
    ubicacion_vie6 = models.ForeignKey(Place, verbose_name="Ubicaciónvie6", on_delete=models.CASCADE, related_name="u_viernes6", null=True, blank=True, default='')
    
class ThirdContenido(models.Model):
    cabecera7 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_7")
    hora7 = models.TextField(max_length=50, verbose_name="hora7", null=True, blank=True, default='')
    maestro_lun7 = models.ForeignKey(Teacher, verbose_name="Maestrolunes7", on_delete=models.CASCADE, related_name="m_lunes7", null=True, blank=True, default='')
    asignatura_lun7 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes7", on_delete=models.CASCADE, related_name="a_lunes7", null=True, blank=True, default='')
    ubicacion_lun7 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes7", on_delete=models.CASCADE, related_name="u_lunes7", null=True, blank=True, default='')
    maestro_mar7 = models.ForeignKey(Teacher, verbose_name="Maestromartes7", on_delete=models.CASCADE, related_name="m_martes7", null=True, blank=True, default='')
    asignatura_mar7 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes7", on_delete=models.CASCADE, related_name="a_martes7", null=True, blank=True, default='')
    ubicacion_mar7 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes7", on_delete=models.CASCADE, related_name="u_martes7", null=True, blank=True, default='')
    maestro_mie7 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles7", on_delete=models.CASCADE, related_name="m_miercoles7", null=True, blank=True, default='')
    asignatura_mie7 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles7", on_delete=models.CASCADE, related_name="a_miercoles7", null=True, blank=True, default='')
    ubicacion_mie7 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles7", on_delete=models.CASCADE, related_name="u_miercoles7", null=True, blank=True, default='')
    maestro_jue7 = models.ForeignKey(Teacher, verbose_name="Maestrojueves7", on_delete=models.CASCADE, related_name="m_jueves7", null=True, blank=True, default='')
    asignatura_jue7 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves7", on_delete=models.CASCADE, related_name="a_jueves7", null=True, blank=True, default='')
    ubicacion_jue7 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves7", on_delete=models.CASCADE, related_name="u_jueves7", null=True, blank=True, default='')
    maestro_vie7 = models.ForeignKey(Teacher, verbose_name="Maestrovie7", on_delete=models.CASCADE, related_name="m_viernes7", null=True, blank=True, default='')
    asignatura_vie7 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie7", on_delete=models.CASCADE, related_name="a_viernes7", null=True, blank=True, default='')
    ubicacion_vie7 = models.ForeignKey(Place, verbose_name="Ubicaciónvie7", on_delete=models.CASCADE, related_name="u_viernes7", null=True, blank=True, default='')
    
    cabecera8 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_8")
    hora8 = models.TextField(max_length=50, verbose_name="hora8", null=True, blank=True, default='')
    maestro_lun8 = models.ForeignKey(Teacher, verbose_name="Maestrolunes8", on_delete=models.CASCADE, related_name="m_lunes8", null=True, blank=True, default='')
    asignatura_lun8 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes8", on_delete=models.CASCADE, related_name="a_lunes8", null=True, blank=True, default='')
    ubicacion_lun8 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes8", on_delete=models.CASCADE, related_name="u_lunes8", null=True, blank=True, default='')
    maestro_mar8 = models.ForeignKey(Teacher, verbose_name="Maestromartes8", on_delete=models.CASCADE, related_name="m_martes8", null=True, blank=True, default='')
    asignatura_mar8 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes8", on_delete=models.CASCADE, related_name="a_martes8", null=True, blank=True, default='')
    ubicacion_mar8 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes8", on_delete=models.CASCADE, related_name="u_martes8", null=True, blank=True, default='')
    maestro_mie8 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles8", on_delete=models.CASCADE, related_name="m_miercoles8", null=True, blank=True, default='')
    asignatura_mie8 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles8", on_delete=models.CASCADE, related_name="a_miercoles8", null=True, blank=True, default='')
    ubicacion_mie8 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles8", on_delete=models.CASCADE, related_name="u_miercoles8", null=True, blank=True, default='')
    maestro_jue8 = models.ForeignKey(Teacher, verbose_name="Maestrojueves8", on_delete=models.CASCADE, related_name="m_jueves8", null=True, blank=True, default='')
    asignatura_jue8 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves8", on_delete=models.CASCADE, related_name="a_jueves8", null=True, blank=True, default='')
    ubicacion_jue8 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves8", on_delete=models.CASCADE, related_name="u_jueves8", null=True, blank=True, default='')
    maestro_vie8 = models.ForeignKey(Teacher, verbose_name="Maestrovie8", on_delete=models.CASCADE, related_name="m_viernes8", null=True, blank=True, default='')
    asignatura_vie8 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie8", on_delete=models.CASCADE, related_name="a_viernes8", null=True, blank=True, default='')
    ubicacion_vie8 = models.ForeignKey(Place, verbose_name="Ubicaciónvie8", on_delete=models.CASCADE, related_name="u_viernes8", null=True, blank=True, default='')

    cabecera9 = models.ForeignKey(Cabecera, null=True, blank=True, on_delete=models.CASCADE, default='', related_name="cab_9")
    hora9 = models.TextField(max_length=50, verbose_name="hora9", null=True, blank=True, default='')
    maestro_lun9 = models.ForeignKey(Teacher, verbose_name="Maestrolunes9", on_delete=models.CASCADE, related_name="m_lunes9", null=True, blank=True, default='')
    asignatura_lun9 = models.ForeignKey(Asignatura, verbose_name="Asignaturalunes9", on_delete=models.CASCADE, related_name="a_lunes9", null=True, blank=True, default='')
    ubicacion_lun9 = models.ForeignKey(Place, verbose_name="Ubicaciónlunes9", on_delete=models.CASCADE, related_name="u_lunes9", null=True, blank=True, default='')
    maestro_mar9 = models.ForeignKey(Teacher, verbose_name="Maestromartes9", on_delete=models.CASCADE, related_name="m_martes9", null=True, blank=True, default='')
    asignatura_mar9 = models.ForeignKey(Asignatura, verbose_name="Asignaturamartes9", on_delete=models.CASCADE, related_name="a_martes9", null=True, blank=True, default='')
    ubicacion_mar9 = models.ForeignKey(Place, verbose_name="Ubicaciónmartes9", on_delete=models.CASCADE, related_name="u_martes9", null=True, blank=True, default='')
    maestro_mie9 = models.ForeignKey(Teacher, verbose_name="Maestromiercoles9", on_delete=models.CASCADE, related_name="m_miercoles9", null=True, blank=True, default='')
    asignatura_mie9 = models.ForeignKey(Asignatura, verbose_name="Asignaturamiercoles9", on_delete=models.CASCADE, related_name="a_miercoles9", null=True, blank=True, default='')
    ubicacion_mie9 = models.ForeignKey(Place, verbose_name="Ubicaciónmiercoles9", on_delete=models.CASCADE, related_name="u_miercoles9", null=True, blank=True, default='')
    maestro_jue9 = models.ForeignKey(Teacher, verbose_name="Maestrojueves9", on_delete=models.CASCADE, related_name="m_jueves9", null=True, blank=True, default='')
    asignatura_jue9 = models.ForeignKey(Asignatura, verbose_name="Asignaturajueves9", on_delete=models.CASCADE, related_name="a_jueves9", null=True, blank=True, default='')
    ubicacion_jue9 = models.ForeignKey(Place, verbose_name="Ubicaciónjueves9", on_delete=models.CASCADE, related_name="u_jueves9", null=True, blank=True, default='')
    maestro_vie9 = models.ForeignKey(Teacher, verbose_name="Maestrovie9", on_delete=models.CASCADE, related_name="m_viernes9", null=True, blank=True, default='')
    asignatura_vie9 = models.ForeignKey(Asignatura, verbose_name="Asignaturavie9", on_delete=models.CASCADE, related_name="a_viernes9", null=True, blank=True, default='')
    ubicacion_vie9 = models.ForeignKey(Place, verbose_name="Ubicaciónvie9", on_delete=models.CASCADE, related_name="u_viernes9", null=True, blank=True, default='')