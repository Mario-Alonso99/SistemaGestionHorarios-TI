from django import forms

#Importamos el Módelo de la Aplicación Students (models.py)
from apps.appDirection.students.models import Student

#Importamos el Formulario de Creación de Django
from django.contrib.auth.forms import UserCreationForm

#Formulario Empleando los campos del Modelo de User y los campos del nuevo Modelo (models.py)
class RegistroForm(UserCreationForm):
	class Meta:
		model = Student
		fields = [
				#fields del Módelo creado
				'matricula',
				'especialidad',
				'cuatrimestre',
				'grupo',
				'estatus',
				'tipo',
				#Fields del Módelo User de Django
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				#labels del Módelo creado
				'matricula': 'Matrícula:',
				'especialidad': 'Especialidad:',
				'cuatrimestre': 'Cuatrimestre:',
				'grupo': 'Grupo:',
				'estatus': 'Estatus:',
				'tipo': 'Tipo:',
				#labels del Módelo User de Django
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}
		widgets = {
			#widgest del Módelo creado
			'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': '20172ITI009', 'required': 'required'}),
			'especialidad': forms.Select(attrs={'class':'form-control'}),
			'cuatrimestre': forms.Select(attrs={'class':'form-control'}),
			'grupo': forms.Select(attrs={'class':'form-control'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
			#widgest del Módelo User de Django
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'mario.blazter99', 'required': 'required'}),
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Mario Alberto', 'required': 'required'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Alonso Alvarado', 'required': 'required'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'mario.blazter99@gmail.com', 'required': 'required'}),
		}