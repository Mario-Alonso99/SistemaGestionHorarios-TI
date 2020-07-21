import django_filters
from apps.appDirection.places.models import Place

class PlaceFilter(django_filters.FilterSet):
	class Meta:
		model = Place
		fields = ['encargado', 'ubicacion', 'tipo', 'nombre']