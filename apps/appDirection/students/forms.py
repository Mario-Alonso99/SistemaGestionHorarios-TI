from django import forms
from apps.appDirection.students.models import Student

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
			'email': 'Email',
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