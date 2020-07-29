import django_filters
from apps.appDirection.teachers.models import Teacher

class TeacherFilter(django_filters.FilterSet):
	class Meta:
		model = Teacher
		fields = ['first_name',  'matricula', 'estatus', 'grado_academico','tjornada','numero_empleado']