from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from comentariosApp.api.serializers import ComentarioSerializer
from comentariosApp.models import Comentarios
from publicacionesApp.models import Autor
from rest_framework import generics 

from django.shortcuts import get_object_or_404


#la clase comentario la trabajamos de manera generica con metodos get y post genericos
#metodo 1
class ComentarioCreate (generics.CreateAPIView ):
    serializer_class = ComentarioSerializer
    def perform_create(self, serializer):
        pk2=self.kwargs['pk2']
        autor=Autor.objects.get(pk=pk2)
        pk=self.kwargs['pk']
        publicacionn=pk
        serializer.save(autores=autor,publicacion=publicacionn)
    
class ComentarioLis(generics.ListCreateAPIView ):
    #queryset = Comentarios. objects. all()
    serializer_class = ComentarioSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return  Comentarios.objects.filter(autores=pk) # me trae todos los comentarios que pertenezcan a ese autor

class ComentariosDetail(generics.ListCreateAPIView): 
    queryset = Comentarios. objects. all()
    serializer_class = ComentarioSerializer
