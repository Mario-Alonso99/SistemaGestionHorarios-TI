from django.db import models

TEACHER_CHOICES_TIPO = (
    ('AP', 'AP'),
    ('TCP', 'TCP'),
)

TEACHER_CHOICES_ESTATUS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)

# Create your models here.
class Teacher(models.Model):
    matricula = models.TextField(max_length=15, verbose_name="Matrícula")
    nombre = models.TextField(max_length=200, verbose_name="Nombre")
    email = models.TextField(max_length=200, verbose_name="Email", null=False, blank=False)
    grado_academico = models.TextField(max_length=200, verbose_name="Grado academico", default='')
    tipo = models.TextField(null=False, blank=False, choices=TEACHER_CHOICES_TIPO, default='AP')
    numero_empleado = models.TextField(max_length=200, verbose_name="Número de empleado", default='')
    password = models.TextField(max_length=200, verbose_name="Contraseña", null=False, blank=False)
    estatus = models.TextField(null=False, blank=False, choices=TEACHER_CHOICES_ESTATUS, default='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        ordering = ['grado_academico', 'tipo']

    def __str__(self):
        return self.nombre