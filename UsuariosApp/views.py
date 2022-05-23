from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView,UpdateView
from .models import  Usuario
from .forms import  FormularioUsuario,PersonaForm
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
    
def cambiarUsuario(request):
    x=request.session.get('_auth_user_id')
     
    usuario=get_object_or_404(Usuario,pk=x)
    if request.method == 'POST':
        formaPersona=PersonaForm(request.POST, instance=usuario)
        if formaPersona.is_valid():
            post=formaPersona.save(commit=False)
            post.is_userp= True
            post.save()
            return redirect('blog:listar-post')
    else:
        
        formaPersona=PersonaForm(instance=usuario)
        
    return render(request, 'usuarios/Vendedor.html',{'formaPersona':formaPersona})