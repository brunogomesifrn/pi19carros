from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
	numero = models.CharField('Número' , max_length=16, blank=True, null=True)

	def __str__(self):
		return self.user.username

class Carros_Diarios(models.Model):
	nome = models.CharField('Nome', max_length=500)
	preco = models.DecimalField(max_digits=7, decimal_places=2)
	imagem = models.ImageField()
	link = models.CharField('Link', max_length=1000)

	def __str__(self):
			return self.nome

class Carros_Comprar(models.Model):
	nome = models.CharField('Nome', max_length=500)
	ano = models.CharField('Ano', max_length=500, blank=True, null=True)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
	imagem = models.ImageField()
	link = models.CharField('Link', max_length=1000)

	def __str__(self):
			return self.nome