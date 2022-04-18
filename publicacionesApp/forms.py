from django.forms import  ModelForm
from .models import Post


class PublicacionForm(ModelForm):
    class Meta:
        model=Post
        fields=['titulo','slug','descripcion','content','imagen','categoria']
        
        
        