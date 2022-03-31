from django.shortcuts import get_object_or_404, render
from .models import *

def home (request):
    post=Post.objects.filter(estado=True)
    return render(request,'publications\publicaciones.html',{'post':post})

def detalles (request,id):
    post=get_object_or_404(Post,id=id)
    #post=Post.objects.get(slug=slug)#the same shit pero sin la comprobacion
    return render(request,'publications\post.html',{'detalles':post})

def autor (request,id):
    autor=get_object_or_404(Autor,pk=id)
    
    # post=Post.objects.filter(estado=True, 
    #                          categoria=Categoria.objects.get(nombre__iexact='VideoJuegos'))
    
    return render(request,'publications\perfilAutor.html',{'autor':autor})