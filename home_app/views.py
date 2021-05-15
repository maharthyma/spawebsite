from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from home_app.forms import UserRegisterForm
from home_app.models import *


def home(request):
    carousel = Carousel.objects.all()
    package = Package.objects.all()
    statistics = Statistics.objects.all()
    review = Review.objects.all()
    about = About_2.objects.all()
    contactUs = ContactUs.objects.all()
    return render(request, 'index.html',
                  {'carousel': carousel, 'package': package, 'statistics': statistics, 'review': review,
                   'about': about, 'contactUs': contactUs})


def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            print(request, f' wecome {username} !!')
            return redirect('home')
        else:
            print(request, f'Invalid Details')
    form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form, 'title': 'Sign in'})


def Signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            htmly = get_template('Email.html')
            d = {'username': username, 'first_name': first_name, 'last_name': last_name}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Register.html', {'form': form, 'title': 'reqister here'})


def checkout(request):
    pass


def portfolio(request):
    contactUs = ContactUs.objects.all()
    return render(request, 'services.html', {'contactUs': contactUs})


def contactus(request):
    contactUs = ContactUs.objects.all()
    about = About.objects.all()

    return render(request, 'contact.html', {'contactUs': contactUs})


def package(request):
    pass


def About_fun(request):
    contactUs = ContactUs.objects.all()
    team = Team.objects.all()
    about_other = About_2.objects.all()
    about = About.objects.all()
    return render(request, 'about.html',
                  {'contactUs': contactUs, 'about': about, 'about_other': about_other, 'team': team})
