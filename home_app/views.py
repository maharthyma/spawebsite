from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'index.html')


def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'Invalid Details')
    form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form, 'title': 'Sign in'})


def singup(request):
    return render(request, 'Register.html')


def checkout(request):
    pass


def portfolio(request):
    return render(request, 'services.html')


def contactus(request):
    return render(request, 'contact.html')


def package(request):
    pass
