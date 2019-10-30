from django.shortcuts import render, redirect
from .form import UserForm, UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario

def home(request):
    return render(request, 'index.html')

def categoria(request):
    return render(request, 'categorias.html')

@login_required
def perfil(request, pk):
    dados = {}
    user = User.objects.get(pk = pk)
    usuario = Usuario.objects.get(user = user.pk)
    dados["usuario"] = usuario
    return render(request, 'perfil.html', dados)


@login_required
def edit_perfil(request, pk):
    dados = {} 
    user = User.objects.get(pk = pk)
    if request.method == 'POST':
        form = UsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil', pk=user.id)
    else:
        form = UsuarioForm(initial={'user':user.id})
    dados['form'] = form
    return render(request, 'edit_perfil.html', dados) 

def cadastro(request):
    logout(request)
    dados = {}
    form = UserForm(initial={'is_active':True})
    dados['form'] = form

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.first_name
            user.set_password(request.POST['password'])
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return redirect('home')

    return render(request, 'Login_Cadastro.html', dados)


def login_(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['first_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("erro")

    return redirect('cadastro')
