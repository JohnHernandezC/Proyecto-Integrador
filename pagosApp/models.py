from django.db import models

from publicacionesApp.models import Post

# Create your models here.

class Producto(models.Model):
    producto = models.CharField(max_length=100, null= False)
    precio = models.DecimalField(max_digits=5 ,decimal_places= 2)

    def __str__(self):
        return self.producto

class Compra(models.Model):
    id = models.CharField(primary_key= True, max_length=100)
    estado = models.CharField(max_length=100)
    codigo_estado = models.CharField(max_length=100)
    producto = models.ForeignKey(to=Post, on_delete= models.SET_NULL, null = True)
    total_de_la_compra = models.DecimalField(max_digits=5 ,decimal_places= 2)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField(max_length=100)
    direccion_cliente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cliente
