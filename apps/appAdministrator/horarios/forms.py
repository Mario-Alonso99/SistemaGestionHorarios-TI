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

class HorarioFormBody1(forms.ModelForm):
	class Meta:
		model = Contenido
		fields = [
			'hora1',
    		'maestro_lun1',
			'asignatura_lun1',
			'ubicacion_lun1',
			'maestro_mar1',
			'asignatura_mar1',
			'ubicacion_mar1',
			'maestro_mie1',
			'asignatura_mie1',
			'ubicacion_mie1',
			'maestro_jue1',
			'asignatura_jue1',
			'ubicacion_jue1',
			'maestro_vie1',
			'asignatura_vie1',
			'ubicacion_vie1',
		]

		labels = {
		
		}

		widgets = {
			'hora1': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun1': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun1': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun1': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar1': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar1': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar1': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie1': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie1': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie1': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue1': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue1': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue1': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie1': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie1': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie1': forms.Select(attrs={'class':'form-control'}),
		}


class HorarioFormBody2(forms.ModelForm):
	class Meta:
		model = Contenido
		fields = [
			'hora2',
    		'maestro_lun2',
			'asignatura_lun2',
			'ubicacion_lun2',
			'maestro_mar2',
			'asignatura_mar2',
			'ubicacion_mar2',
			'maestro_mie2',
			'asignatura_mie2',
			'ubicacion_mie2',
			'maestro_jue2',
			'asignatura_jue2',
			'ubicacion_jue2',
			'maestro_vie2',
			'asignatura_vie2',
			'ubicacion_vie2',
		]

		labels = {
		
		}

		widgets = {
			'hora2': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun2': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun2': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun2': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar2': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar2': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar2': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie2': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie2': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie2': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue2': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue2': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue2': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie2': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie2': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie2': forms.Select(attrs={'class':'form-control'}),
		}


class HorarioFormBody3(forms.ModelForm):
	class Meta:
		model = Contenido
		fields = [
			'hora3',
    		'maestro_lun3',
			'asignatura_lun3',
			'ubicacion_lun3',
			'maestro_mar3',
			'asignatura_mar3',
			'ubicacion_mar3',
			'maestro_mie3',
			'asignatura_mie3',
			'ubicacion_mie3',
			'maestro_jue3',
			'asignatura_jue3',
			'ubicacion_jue3',
			'maestro_vie3',
			'asignatura_vie3',
			'ubicacion_vie3',
		]

		labels = {
		
		}

		widgets = {
			'hora3': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun3': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun3': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun3': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar3': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar3': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar3': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie3': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie3': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie3': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue3': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue3': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue3': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie3': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie3': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie3': forms.Select(attrs={'class':'form-control'}),
		}