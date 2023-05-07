from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from . views import index
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.handlelogin, name = 'handlelogin'),
    path('logout', views.handlelogout, name = 'handlelogout'),
    path('Admin', views.admin, name = 'admin'),
    path('signup', views.handlesignup, name = 'handlesignup')
]