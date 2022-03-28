from django.db import models

from ckeditor.fields import RichTextField


class Categoria (models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')
    def __str__(self):
        return self.nombre
    
    
class Autor (models.Model):
    nombres = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    paginaW = models.URLField(null=True, blank=True)
    email= models.EmailField(default=None)
    estado= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Autor')
        verbose_name_plural = ('Autores')
    def __str__(self):
        return self.nombres   

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    slug= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    content = RichTextField(default=None)
    imagen= models.URLField(max_length=300)
    autor= models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado',default=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
    def __str__(self):
        return self.titulo 
