from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.forms import ValoresForm

from app.models import Valores

# Create your views here.
def home(request):
  return render(request, 'home.html')

def cadastro(request):
  return render(request, 'cadastro.html')

def store(request):
  data ={}
  if(request.POST['password'] != request.POST['password-conf']):
    data['msg'] = 'Senha e Confirmação são diferentes'
    data['class'] = 'alert-danger'
  else:
    user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
    user.first_name = request.POST['name']
    user.save()
    data['msg'] = 'Usuário cadastrado com sucesso'
    data['class'] = 'alert-success'
  return render(request, 'cadastro.html', data)

def painel(request):
  return render(request, 'painel.html')

def validacao(request):
  user = authenticate(username = request.POST['user'], password = request.POST['password'])
  if user is not None:
    login(request, user)
    return redirect('/formdados/')
  return render(request, 'painel.html')

def logouts(request):
  logout(request)
  return redirect('/painel/')

def formdados(request):
  form = ValoresForm()
  val = {
    'form': form,
  }
  return render(request, 'formdados/inicio.html', val)

def newdados(request):
  form = ValoresForm(request.POST or None)
  if (form.is_valid()):
    form.save()
  form = ValoresForm()
  val = {
    'form': form,
  }
  return render(request, 'formdados/inicio.html', val) 
