from django.forms import  ModelForm
from .models import Post,solicitudes
from django import forms

class PublicacionForm(ModelForm):
    class Meta:
        model=Post
        fields=['titulo','slug','descripcion','content','imagen','categoria','precio']
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
            'precio': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Agregue el precio',
            
                }  
            )
            
            
            
        }
class Solicita(ModelForm):
    class Meta:
        model=solicitudes
        fields=['descripcion']
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'clase':'form-control',
                     'placeholder':'Agrega una brevedescripcion de lo que buscas',
            
                }
            ),
        }
        
class SolicitaE(ModelForm):
    class Meta:
        model=solicitudes
        fields=['aceptado']
        