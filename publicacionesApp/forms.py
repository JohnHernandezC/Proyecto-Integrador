from django.forms import  ModelForm
from .models import Post
from django import forms

class PublicacionForm(ModelForm):
    class Meta:
        model=Post
        fields=['titulo','slug','descripcion','content','imagen','categoria']
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'clase':'form-control',
                     'placeholder':'Titulo del servicio',
            
                }
            ),
            'slug': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Elija un Slug',
                     'required':'required',
            
                }  
            ),
            'descripcion': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Agregue una breve descripcion',
                     'required':'required',
            
                }  
            ),
            'content': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Agregue el contenido',
            
                }  
            ),
            'imagen': forms.ClearableFileInput(),
            
            
            
        }
        
        
        