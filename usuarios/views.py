from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas nao coincidem.')
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario ja existe.')
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')

        return redirect(reverse('login'))
    
        # TODO: validar forca da senha

def login(request):
    pass

