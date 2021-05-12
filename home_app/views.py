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
    pass


def contactus(request):
    pass


def package(request):
    pass
