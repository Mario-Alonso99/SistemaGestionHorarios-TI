from django import forms

#Empleamos los modelos creados
from apps.appAdministrator.horarios.models import Cabecera, Contenido

class HorarioFormHead(forms.ModelForm):
	class Meta:
		model = Cabecera
		fields = [
			'id_usuario',
			'fecha',
			'especialidad',
			'cuatrimestre',
			'grupo',
			'anexos',
		]

		labels = {			
			'id_usuario': 'Id Usuario',
			'fecha': 'Fecha',
			'especialidad': 'Especialidad',
			'cuatrimestre': 'Cuatrimestre',
			'grupo': 'Grupo',
			'anexos': 'Anexos',
		}

		widgets = {
			'id_usuario': forms.TextInput(attrs={'class':'form-control'}),
			'fecha': forms.TextInput(attrs={'class':'form-control'}),
			'especialidad': forms.Select(attrs={'class':'form-control'}),
			'cuatrimestre': forms.Select(attrs={'class':'form-control'}),
			'grupo': forms.Select(attrs={'class':'form-control'}),
			'anexos': forms.TextInput(attrs={'class':'form-control'}),
		}

class HorarioFormBody(forms.ModelForm):
	class Meta:
		model = Contenido
		fields = [
			'hora',
    		'maestro_lun',
			'asignatura_lun',
			'ubicacion_lun',
			'maestro_mar',
			'asignatura_mar',
			'ubicacion_mar',
			'maestro_mie',
			'asignatura_mie',
			'ubicacion_mie',
			'maestro_jue',
			'asignatura_jue',
			'ubicacion_jue',
			'maestro_vie',
			'asignatura_vie',
			'ubicacion_vie',
		]

		labels = {
		
		}

		widgets = {
			'hora': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie': forms.Select(attrs={'class':'form-control'}),
		}