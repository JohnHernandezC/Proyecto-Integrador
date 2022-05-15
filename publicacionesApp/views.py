from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from . forms import PublicacionForm,Solicita, SolicitaE
from comentariosApp.models import Comentarios
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q

def home (request):
    
    print(request.GET)#con esto podemos capturar como esta llegano un valor enviado pos Get
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True)
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset)#Q es para englobar todo y user mas de una consulta con el |
            ).distinct()
        
    paginator=Paginator(post,10)
    page=request.GET.get('page')
    post=paginator.get_page(page)
    return render(request,'publications\publicaciones.html',{'post':post})


def detalles (request,id):
    print("Id"+ str(id))
    post=get_object_or_404(Post,id=id)
    
    slug1=post.slug
    comentarios=Comentarios.objects.filter(active=True, 
                              publicacion=id)
    solicitud=solicitudes.objects.filter(postS=id, usuario=request.user.pk)
    
    postRecomendados=Post.objects.filter(estado=True, slug=slug1)
    #post=Post.objects.get(slug=slug)#the same shit pero sin la comprobacion
    return render(request,'publications\post.html',{'detalles':post,'recomendaciones':postRecomendados,'comentarios':comentarios,'solicitud':solicitud})

def solicitudesP(request,id,idA):
    
    
    
    if request.method == 'POST':
        formS=Solicita(request.POST)
        post_instance = get_object_or_404(Post, id=id)
        #de la vista nuevo
        if formS.is_valid():
            post=formS.save(commit=False)
            post.postS=post_instance
            post.usuario=request.user.pk
            post.ofertante=idA
           
            
            
            post.save()
            messages.success(request,'Solicitud realizada con exito')
            return redirect('inicio:index-principal')
        
    else:
        form=Solicita()
    return render(request, 'publications/SolicitudM.html',{'formSolicitud':form})
    


def autor (request,id):
    
    autor=get_object_or_404(Autor,pk=id)
    
    post=Post.objects.filter(estado=True, 
                              autor=Autor.objects.get(id=id))
    
    return render(request,'publications\perfilAutor.html',{'autor':autor, 'post':post})

def crearPost (request):
    print("aqui")
    print(request.user.username)
    courrent_user=get_object_or_404(Autor,pk=request.user.pk)
    print("////////////////////////////////////////")
    x=request.session.get('_auth_user_id')
    print('primero')
    print(courrent_user)
    print('segundo')
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

def controlMisPost (request):
    x=request.session.get('_auth_user_id')
    solicitud=solicitudes.objects.filter(ofertante=x)
    return render(request,'publications\AceptarDenegar.html',{'post':solicitud})

def aceptarSolicitud(request,id):
    form=None
    error=None
    try:
        solicitud=solicitudes.objects.get(id=id)# solo trae un objeto filtrado por la variable que le pasamos
        if request.method=='GET':
            form=SolicitaE(instance=solicitud)
        else:
            form=SolicitaE(request.POST, instance=solicitud)
            if form.is_valid(): 
                form.save()
                return redirect('blog:listar-Solicitudes')
    except ObjectDoesNotExist as e:
        error=e
        
    return render(request,'publications/crearPublicaciones.html',{'formaPersona':form,'error':error})

def denegarSolicitud(request,id):
    solicitud=solicitudes.objects.get(id=id)
    if request.method=='POST': 
        solicitud.delete()
        return redirect('blog:listar-post')
    return render(request,'publications/eliminarPost.html',{'post':solicitud})
    
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


    
    



    

    
    
