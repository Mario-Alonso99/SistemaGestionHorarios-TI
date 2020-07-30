from import_export import resources
from .models import Administrator

class AdministratorResource(resources.ModelResource):
    class Meta:
        model = Administrator