from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
	numero = models.CharField('Número' , max_length=16, blank=True, null=True)

	def __str__(self):
		return self.user.username