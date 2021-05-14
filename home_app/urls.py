from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views

from home_app.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'login', Login, name='login'),
    url(r'singup', Signup, name='singup'),
    url(r'logout', views.LogoutView, name='logout'),
    url(r'checkout', checkout, name='checkout'),
    url(r'About', About, name='About'),
    url(r'portfolio', portfolio, name='portfolio'),
    url(r'contactus', contactus, name='contactus'),
    url(r'package', package, name='package'),
]
