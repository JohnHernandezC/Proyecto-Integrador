from django.shortcuts import get_object_or_404, render
from .models import *

def home (request):
    post=Post.objects.filter(estado=True)
    return render(request,'publications\publicaciones.html',{'post':post})

def detalles (request,id):
    post=get_object_or_404(Post,id=id)
    slug1=post.slug
    imagenA=post.autor
    
    
    postRecomendados=Post.objects.filter(estado=True, slug=slug1)
    #post=Post.objects.get(slug=slug)#the same shit pero sin la comprobacion
    return render(request,'publications\post.html',{'detalles':post,'recomendaciones':postRecomendados,'fotos':imagenA})

def autor (request,id):
    autor=get_object_or_404(Autor,pk=id)
    
    post=Post.objects.filter(estado=True, 
                              autor=Autor.objects.get(id=id))
    
    return render(request,'publications\perfilAutor.html',{'autor':autor, 'post':post})
