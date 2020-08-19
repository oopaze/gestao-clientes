from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return HttpResponse('Home')

def cadastrar_usuario(request):
    form = ClienteForm(request.POST or None)
    return render(request, 'registrar.html', {'form':form})

def ler_usuario(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def atualizar_usuario(request):
    return HttpResponse('Atualizar Usuario')

def deletar_usuario(request):
    return HttpResponse('Deletar Usuario')
