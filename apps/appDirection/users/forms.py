from django import forms
#Lineas Extras
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#Lineas Extras, Registro de Campos Extras en el Administrador de Django
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

class FormLogin(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(FormLogin, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'