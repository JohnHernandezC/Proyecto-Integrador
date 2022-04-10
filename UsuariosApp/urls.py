
from django.urls import path
from .views import *

urlpatterns = [
    
    path('crearU/',registrarUsuario.as_view(),name='crear-User')
  
]


