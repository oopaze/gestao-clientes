from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'index.html')

def sair(request):
    logout(request)
    return redirect('inicio')
