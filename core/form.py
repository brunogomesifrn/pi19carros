from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']
		widgets = {
		'is_active': forms.HiddenInput(),
		'is_staff': forms.HiddenInput(),
		'is_superuser': forms.HiddenInput(),
		}
		
