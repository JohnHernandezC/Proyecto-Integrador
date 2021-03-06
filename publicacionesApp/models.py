from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator,MaxValueValidator
from UsuariosApp.models import Usuario


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
    nickname = models.CharField(max_length=50,null=True, blank = True)
    usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)
    paginaW = models.URLField(null=True, blank=True)
    estudios= models.CharField(max_length=500,null=True, blank = True)
    universidad= models.CharField(max_length=50,null=True, blank = True)
    conocimientos= models.CharField(max_length=500,null=True, blank = True)
    estado= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Autor')
        verbose_name_plural = ('Autores')
    def __str__(self):
        return self.usuario.username

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    slug= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    content = RichTextField(default=None)
    imagen = models.ImageField('Imagen de post', max_length=200,blank = True,null = True)
    autor= models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    estado = models.BooleanField('Publicado/No publicado',default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
    def __str__(self):
        return self.titulo 

class solicitudes(models.Model):
    descripcion= models.TextField(max_length=500)
    aceptado= models.BooleanField(default=False)
    postS= models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario=models.IntegerField()
    ofertante=models.IntegerField()
    class Meta:
        verbose_name = ('Solicitud')
        verbose_name_plural = ('Solicitudes')
    def __str__(self):
        return str(self.postS)
    