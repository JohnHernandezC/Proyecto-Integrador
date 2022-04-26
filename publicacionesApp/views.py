from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from . forms import PublicacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

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
    print(x)
    if request.method == 'POST':
        forms1=PublicacionForm(request.POST,request.FILES)#obtener la informacion que esta contenida en el metodo POST 
        print(forms1)
        #de ls vista nuevo
        if forms1.is_valid():
            post=forms1.save(commit=False)
            post.autor=courrent_user
            post.save()
            messages.success(request,'Post creado con exito')
            return redirect('inicio:index-principal')
        
    else:
        form=PublicacionForm()
    return render(request, 'publications/crearPublicaciones.html',{'formaPersona':form})

def listarMisPost (request):
    x=request.session.get('_auth_user_id')
    lpost=Post.objects.filter(autor=x)
    print(lpost)
    return render(request,'publications\listarMisPost.html',{'post':lpost})

def editarPost (request,id):
    form=None
    error=None
    try:
        postE=Post.objects.get(id=id)# solo trae un objeto filtrado por la variable que le pasamos
        if request.method=='GET':
            form=PublicacionForm(instance=postE)
        else:
            form=PublicacionForm(request.POST, instance=postE)
            if form.is_valid(): 
                form.save()
                return redirect('blog:listar-post')
    except ObjectDoesNotExist as e:
        error=e
        
    return render(request,'publications/crearPublicaciones.html',{'formaPersona':form,'error':error})

def eliminarPost (request,id):
    posts=Post.objects.get(id=id)
    if request.method=='POST':
        #eliminacion logica
        #post.estado=false
        #post.save() 
        posts.delete()
        return redirect('blog:listar-post')
    return render(request,'publications/eliminarPost.html',{'post':posts})



    

    
    
