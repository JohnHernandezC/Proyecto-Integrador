from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from . forms import PublicacionForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home (request):
    post=Post.objects.filter(estado=True)
    return render(request,'publications\publicaciones.html',{'post':post})


def detalles (request,id):
    post=get_object_or_404(Post,id=id)
    slug1=post.slug
    
    postRecomendados=Post.objects.filter(estado=True, slug=slug1)
    #post=Post.objects.get(slug=slug)#the same shit pero sin la comprobacion
    return render(request,'publications\post.html',{'detalles':post,'recomendaciones':postRecomendados})



def autor (request,id):
    
    autor=get_object_or_404(Autor,pk=id)
    
    post=Post.objects.filter(estado=True, 
                              autor=Autor.objects.get(id=id))
    
    return render(request,'publications\perfilAutor.html',{'autor':autor, 'post':post})

def crearPost (request):
    courrent_user=get_object_or_404(Autor,pk=request.user.pk)
    print("////////////////////////////////////////")
    x=request.session.get('_auth_user_id')
    print(courrent_user)
    if request.method == 'POST':
        forms1=PublicacionForm(request.POST)#obtener la informacion que esta contenida en el metodo POST 
        print(forms1)
        #de ls vista nuevo
        if forms1.is_valid():#validar si el formulario es valido
            post=forms1.save(commit=False)
            post.autor=courrent_user
            post.save()
            messages.success(request,'Post creado con exito')
            return redirect('inicio:index-principal')
        
    else:
        form=PublicacionForm()
    return render(request, 'publications/crearPublicaciones.html',{'formaPersona':form})

    
    
