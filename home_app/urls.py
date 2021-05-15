from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views
from django.conf.urls.static import static

from home_app.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'login', Login, name='login'),
    url(r'singup', Signup, name='singup'),
    url(r'logout', views.LogoutView, name='logout'),
    url(r'checkout', checkout, name='checkout'),
    url(r'About', About_fun, name='About'),
    url(r'reserve', reserve, name='reserve'),
    url(r'portfolio', portfolio_fun, name='portfolio'),
    url(r'contactus', contactus, name='contactus'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
