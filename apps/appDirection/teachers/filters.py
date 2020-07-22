import django_filters
from apps.appDirection.teachers.models import Teacher

class TeacherFilter(django_filters.FilterSet):
	class Meta:
		model = Teacher
		fields = ['nombre', 'matricula', 'estatus', 'grado_academico','tipo','numero_empleado']