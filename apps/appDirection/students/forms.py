from django import forms
from apps.appDirection.students.models import Student

#Lineas del formulario de registro de Administradores
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Módelo para formulario de Registro de Estudiantes
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'matricula',
			'nombre',
			'especialidad',
			'cuatrimestre',
			'grupo',
			'email',
			'password',
			'estatus',
		]

		labels = {
			'matricula': 'Matrícula',
			'nombre': 'Nombre',
			'especialidad': 'Especialidad',
			'cuatrimestre': 'Cuatrimestre',
			'grupo': 'Grupo',
			'email': 'Correo electrónico',
			'password': 'Contraseña',
			'estatus': 'Estatus',
		}

		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'especialidad': forms.Select(attrs={'class':'form-control'}),
			'cuatrimestre': forms.Select(attrs={'class':'form-control'}),
			'grupo': forms.Select(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
		}

#Módelo para formulario de Registro de Administrador
class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}