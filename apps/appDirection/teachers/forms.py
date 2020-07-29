from django import forms
from apps.appDirection.teachers.models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = [
			#fields del Módelo creado
			'matricula',
			'grado_academico',
			'tjornada',
			'numero_empleado',
			'estatus',
			
			#Fields del Módelo User de Django
			'username',
			'first_name',
			'last_name',
			'email',
			'password',	
			
		]

		labels = {
			#labels del Módelo creado
			'matricula': 'Matrícula',
			'grado_academico': 'Grado academico',
			'tjornada': 'Tipo',
			'numero_empleado': 'Número de empleado',
			'estatus' : 'Estatus',
			
			#labels del Módelo User de Django
			'username': 'Nombre de usuario:',
			'first_name': 'Nombre:',
			'last_name': 'Apellidos:',
			'email': 'Correo Electrónico:',
			'password': 'Contraseña:',

		}

		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': '20172ITI005', 'required': 'required'}),
			'grado_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Licenciatura', 'required': 'required'}),
			'tjornada': forms.Select(attrs={'class':'form-control'}),
			'numero_empleado': forms.TextInput(attrs={'class':'form-control', 'placeholder': '001', 'required': 'required'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
			
			#widgest del Módelo User de Django
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'daniela.08', 'required': 'required'}),
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Daniela', 'required': 'required'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Muñoz Hernández', 'required': 'required'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'dan.08@gmail.com', 'required': 'required'}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': '************', 'required': 'required'}),
		
		}