
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('crearU/',registrarUsuario.as_view(),name='crear-User'),
    path('login/',LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='inicio/index.html'), name='logout'),
  
]


