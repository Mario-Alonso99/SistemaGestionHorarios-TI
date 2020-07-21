import django_filters
from apps.appDirection.students.models import Student

class StudentFilter(django_filters.FilterSet):
	class Meta:
		model = Student
		fields = ['nombre', 'matricula', 'especialidad', 'cuatrimestre', 'grupo']