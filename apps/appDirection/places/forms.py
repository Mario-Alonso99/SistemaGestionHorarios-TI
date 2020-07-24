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
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'P7', 'required': 'required'}),
			'tipo': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
			'encargado': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
			'ubicacion': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
		}