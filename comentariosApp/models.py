from django.db import models
from publicacionesApp.models import Autor
from django.core.validators import MinValueValidator,MaxValueValidator


class Comentarios (models.Model):
    calificacion=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto=models.CharField(max_length=250, null=True)
    autores=models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="comentarios")
    publicacion=models.IntegerField()
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)  
    update=models.DateField(auto_now_add=True) 
    def __str__(self):
        return str(self.calificacion)+" "+str(self.autores.usuario.nombres) 
