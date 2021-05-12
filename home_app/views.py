from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


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
