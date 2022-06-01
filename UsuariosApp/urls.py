
from django.urls import path
from .views import *

from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('crearU/',registrarUsuario.as_view(),name='crear-User'),
    path('editarU/<int:pk>',login_required(ActualizarUsuario.as_view()),name='editarUsuario'),
    path('ofertante',login_required(cambiarUsuario),name='CambiarTipoUsuario'),
  
]


