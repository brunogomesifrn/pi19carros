from django.shortcuts import render, redirect
from .form import UserForm

def home(request):
	return render(request, 'index.html')

def categoria(request):
	return render(request, 'categorias.html')

def perfil(request):
	return render(request, 'perfil.html')

def login_cadastro(request):
	dados = {}
	form = UserForm()
	dados['form'] = form

	if request.method == 'POST':
		form = UserForm(data=request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.first_name
			user.save()
			return redirect('home')

	return render(request, 'Login_Cadastro.html', dados)
