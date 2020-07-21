from django import forms
from apps.appDirection.places.models import Place

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = [
			'nombre',
			'tipo',
			'encargado',
			'ubicacion',
		]

		labels = {
			'nombre': 'Nombre',
			'tipo': 'Tipo',
			'encargado': 'Responsable',
			'ubicacion': 'Ubicación',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.Select(attrs={'class':'form-control'}),
			'encargado': forms.Select(attrs={'class':'form-control'}),
			'ubicacion': forms.Select(attrs={'class':'form-control'}),
		}