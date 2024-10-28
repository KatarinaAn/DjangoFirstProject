from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.shortcuts import render

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    
]
