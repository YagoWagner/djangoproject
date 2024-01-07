from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Usuario

def cadastro(request):
    return HttpResponse('Você está na página de cadastro')


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status' : status, })


def home(request):
    return HttpResponse('Você está na home do Usuario')


def salvar(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    idade = request.POST.get('idade')
    try: 
        usuario = Usuario(
            nome = nome,
            sobrenome = sobrenome,
            idade = idade
        )

        usuario.save()

        return redirect('/usuario/login?status=1')
    except:
        return redirect('/usuario/login?status=2')
    

