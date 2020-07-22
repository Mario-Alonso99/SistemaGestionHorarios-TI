from django import forms
from apps.appDirection.teachers.models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = [
			'matricula',
			'nombre',
            'email',
			'grado_academico',
			'tipo',
			'numero_empleado',
            'password',
			'estatus',
		]

		labels = {
			'matricula': 'Matrícula',
			'nombre': 'Nombre',
            'email' : 'Email',
			'grado_academico': 'Grado academico',
			'tipo': 'Tipo',
			'numero_empleado': 'Número de empleado',
            'password' : 'Contraseña',
			'estatus' : 'Estatus',

		}

		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
			'grado_academico': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.Select(attrs={'class':'form-control'}),
			'numero_empleado': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
		}