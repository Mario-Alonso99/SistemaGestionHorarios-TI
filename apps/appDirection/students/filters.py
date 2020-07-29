import django_filters

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appDirection.students.models import Student

class StudentFilter(django_filters.FilterSet):
	class Meta:
		model = Student
		fields = ['first_name', 'matricula', 'especialidad', 'cuatrimestre', 'grupo']