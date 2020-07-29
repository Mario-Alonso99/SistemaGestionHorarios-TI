import django_filters
from apps.appDirection.asignaturas.models import Asignatura

class AsignaturaFilter(django_filters.FilterSet):
	class Meta:
		model = Asignatura
		fields = ['especialidad', 'cuatrimestre', 'nombre']