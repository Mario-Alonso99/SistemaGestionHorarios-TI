from django import forms
from apps.appDirection.asignaturas.models import Asignatura

class AsignaturaForm(forms.ModelForm):
	class Meta:
		model = Asignatura
		fields = [
			'nombre',
			'especialidad',
			'cuatrimestre',
			
		]

		labels = {
			'nombre': 'Nombre',
			'especialidad': 'Especialidad',
			'cuatrimestre': 'Cuatrimestre',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Administración de proyectos', 'required': 'required'}),
			'especialidad': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
			'cuatrimestre': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
		}