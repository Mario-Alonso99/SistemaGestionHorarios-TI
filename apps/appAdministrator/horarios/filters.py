import django_filters

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appAdministrator.horarios.models import Cabecera

class HorarioFilter(django_filters.FilterSet):
	class Meta:
		model = Cabecera
		fields = ['especialidad', 'cuatrimestre', 'grupo']