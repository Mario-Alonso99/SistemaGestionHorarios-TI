import django_filters
from apps.appDirection.administrators.models import Administrator

class AdministratorFilter(django_filters.FilterSet):
	class Meta:
		model = Administrator
		fields = ['first_name',  'matricula', 'estatus', 'numero_empleado']