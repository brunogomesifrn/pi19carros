from django.contrib import admin
from .models import Usuario, Carros_Comprar, Carros_Diarios, Categorias, Cor

admin.site.register(Usuario)
admin.site.register(Cor)
admin.site.register(Categorias)
admin.site.register(Carros_Comprar)
admin.site.register(Carros_Diarios)

