from django.views.generic import CreateView
from .models import  Usuario
from .forms import  FormularioUsuario
from django.urls import reverse_lazy

class registrarUsuario(CreateView):
    model= Usuario
    form_class= FormularioUsuario
    template_name = 'usuarios\Register.html'
    success_url=reverse_lazy('inicio:index-principal')
    