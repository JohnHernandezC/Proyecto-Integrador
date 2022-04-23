from django.views.generic import CreateView,UpdateView
from .models import  Usuario
from .forms import  FormularioUsuario
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


class registrarUsuario(CreateView):
    model= Usuario
    form_class= FormularioUsuario
    template_name = 'usuarios\Register.html'
    success_url=reverse_lazy('inicio:index-principal')
    

class ActualizarUsuario(UpdateView):
    model=Usuario
    template_name = 'usuarios\Register.html'
    form_class=FormularioUsuario
    success_url=reverse_lazy('inicio:index-principal') 