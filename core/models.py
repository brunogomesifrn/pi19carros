from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	endereco = models.CharField('Endereço', max_length=100)
	imagem_perfil = models.ImageField('Imagem', upload_to='uploads/')