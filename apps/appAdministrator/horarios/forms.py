from django import forms

#Empleamos los modelos creados
from apps.appAdministrator.horarios.models import Cabecera, Contenido, SecondContenido, ThirdContenido

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


class HorarioFormBody4(forms.ModelForm):
	class Meta:
		model = SecondContenido
		fields = [
			'hora4',
    		'maestro_lun4',
			'asignatura_lun4',
			'ubicacion_lun4',
			'maestro_mar4',
			'asignatura_mar4',
			'ubicacion_mar4',
			'maestro_mie4',
			'asignatura_mie4',
			'ubicacion_mie4',
			'maestro_jue4',
			'asignatura_jue4',
			'ubicacion_jue4',
			'maestro_vie4',
			'asignatura_vie4',
			'ubicacion_vie4',
		]

		labels = {
		
		}

		widgets = {
			'hora4': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun4': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun4': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun4': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar4': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar4': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar4': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie4': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie4': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie4': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue4': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue4': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue4': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie4': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie4': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie4': forms.Select(attrs={'class':'form-control'}),
		}

class HorarioFormBody5(forms.ModelForm):
	class Meta:
		model = SecondContenido
		fields = [
			'hora5',
    		'maestro_lun5',
			'asignatura_lun5',
			'ubicacion_lun5',
			'maestro_mar5',
			'asignatura_mar5',
			'ubicacion_mar5',
			'maestro_mie5',
			'asignatura_mie5',
			'ubicacion_mie5',
			'maestro_jue5',
			'asignatura_jue5',
			'ubicacion_jue5',
			'maestro_vie5',
			'asignatura_vie5',
			'ubicacion_vie5',
		]

		labels = {
		
		}

		widgets = {
			'hora5': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun5': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun5': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun5': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar5': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar5': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar5': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie5': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie5': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie5': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue5': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue5': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue5': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie5': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie5': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie5': forms.Select(attrs={'class':'form-control'}),
		}


class HorarioFormBody6(forms.ModelForm):
	class Meta:
		model = SecondContenido
		fields = [
			'hora6',
    		'maestro_lun6',
			'asignatura_lun6',
			'ubicacion_lun6',
			'maestro_mar6',
			'asignatura_mar6',
			'ubicacion_mar6',
			'maestro_mie6',
			'asignatura_mie6',
			'ubicacion_mie6',
			'maestro_jue6',
			'asignatura_jue6',
			'ubicacion_jue6',
			'maestro_vie6',
			'asignatura_vie6',
			'ubicacion_vie6',
		]

		labels = {
		
		}

		widgets = {
			'hora6': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun6': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun6': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun6': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar6': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar6': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar6': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie6': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie6': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie6': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue6': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue6': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue6': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie6': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie6': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie6': forms.Select(attrs={'class':'form-control'}),
		}

class HorarioFormBody7(forms.ModelForm):
	class Meta:
		model = ThirdContenido
		fields = [
			'hora7',
    		'maestro_lun7',
			'asignatura_lun7',
			'ubicacion_lun7',
			'maestro_mar7',
			'asignatura_mar7',
			'ubicacion_mar7',
			'maestro_mie7',
			'asignatura_mie7',
			'ubicacion_mie7',
			'maestro_jue7',
			'asignatura_jue7',
			'ubicacion_jue7',
			'maestro_vie7',
			'asignatura_vie7',
			'ubicacion_vie7',
		]

		labels = {
		
		}

		widgets = {
			'hora7': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun7': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun7': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun7': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar7': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar7': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar7': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie7': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie7': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie7': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue7': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue7': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue7': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie7': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie7': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie7': forms.Select(attrs={'class':'form-control'}),
		}

class HorarioFormBody8(forms.ModelForm):
	class Meta:
		model = ThirdContenido
		fields = [
			'hora8',
    		'maestro_lun8',
			'asignatura_lun8',
			'ubicacion_lun8',
			'maestro_mar8',
			'asignatura_mar8',
			'ubicacion_mar8',
			'maestro_mie8',
			'asignatura_mie8',
			'ubicacion_mie8',
			'maestro_jue8',
			'asignatura_jue8',
			'ubicacion_jue8',
			'maestro_vie8',
			'asignatura_vie8',
			'ubicacion_vie8',
		]

		labels = {
		
		}

		widgets = {
			'hora8': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun8': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun8': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun8': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar8': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar8': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar8': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie8': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie8': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie8': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue8': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue8': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue8': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie8': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie8': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie8': forms.Select(attrs={'class':'form-control'}),
		}

class HorarioFormBody9(forms.ModelForm):
	class Meta:
		model = ThirdContenido
		fields = [
			'hora9',
    		'maestro_lun9',
			'asignatura_lun9',
			'ubicacion_lun9',
			'maestro_mar9',
			'asignatura_mar9',
			'ubicacion_mar9',
			'maestro_mie9',
			'asignatura_mie9',
			'ubicacion_mie9',
			'maestro_jue9',
			'asignatura_jue9',
			'ubicacion_jue9',
			'maestro_vie9',
			'asignatura_vie9',
			'ubicacion_vie9',
		]

		labels = {
		
		}

		widgets = {
			'hora9': forms.TextInput(attrs={'class':'form-control'}),
    		'maestro_lun9': forms.Select(attrs={'class':'form-control'}),
			'asignatura_lun9': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_lun9': forms.Select(attrs={'class':'form-control'}),
			'maestro_mar9': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mar9': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mar9': forms.Select(attrs={'class':'form-control'}),
			'maestro_mie9': forms.Select(attrs={'class':'form-control'}),
			'asignatura_mie9': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_mie9': forms.Select(attrs={'class':'form-control'}),
			'maestro_jue9': forms.Select(attrs={'class':'form-control'}),
			'asignatura_jue9': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_jue9': forms.Select(attrs={'class':'form-control'}),
			'maestro_vie9': forms.Select(attrs={'class':'form-control'}),
			'asignatura_vie9': forms.Select(attrs={'class':'form-control'}),
			'ubicacion_vie9': forms.Select(attrs={'class':'form-control'}),
		}