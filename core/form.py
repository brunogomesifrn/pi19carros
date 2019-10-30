from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Usuario 


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']
		widgets = {
		'is_active': forms.HiddenInput(),
		'is_staff': forms.HiddenInput(),
		'is_superuser': forms.HiddenInput(),
		}
		

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['user', 'endereco', 'numero']
		widgets = {
		'user': forms.HiddenInput(),
		'endereco': forms.TextInput(attrs={'class':'form-control'}),
		'numero': forms.TextInput(attrs={'class':'form-control'}),
		
		}


# class FotoForm(ModelForm):
# 	class Meta:
# 		model = Usuario
# 		fields = ['imagem_perfil']
# 		widgets = {
# 			'imagem_perfil': forms.FileInput(attrs={'class':'form-control'}),
# 		}
		
