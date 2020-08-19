from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return HttpResponse('Home')

def ler_usuario(request):
    clientes = Cliente.objects.all()
    return render(request, 'CRUD/clientes.html', {'clientes': clientes})

def cadastrar_usuario(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('ler_usuario')

    return render(request, 'CRUD/registrar_cliente.html', {'form':form})

def atualizar_usuario(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('ler_usuario')

    return render(request, 'CRUD/atualizar_cliente.html', {'form':form})

def deletar_usuario(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ler_usuario')
    return render(request, 'CRUD/deletar_cliente.html', {'form':form})
