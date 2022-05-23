from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class FormularioUsuario(forms.ModelForm):
    
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput(
        attrs={
            'clase':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
        
    ))
    
    password2 = forms.CharField(label="contraseña de confirmacion", widget=forms.PasswordInput(
        attrs={
            'clase':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id':'password2',
            'required':'required',
        }
        
    ))
    class Meta:
        model=Usuario
        fields=('email','username','nombres','apellidos','imagen')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su correo',
            
                }
            ),
            'nombres': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su nombre',
                     'required':'required',
            
                }  
            ),
            'apellidos': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su apellido',
                     'required':'required',
            
                }  
            ),
            'username': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su nombre de usuario',
            
                }  
            )
            ,
            'imagen': forms.ClearableFileInput(),
            
            
        }
        
    def clean_password2(self):
        #validacion de contraseña (valida que ambas contraseñas sean iguales)
        password1=self.cleaned_data.get('password1')#cleaned_data es donde estan almacenados los datos que se lamacenaron desde el formulario y se obtienen con el get y la key
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden')
        return password2
    
    def save(self,commit=True):
        print(self.cleaned_data)
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])#set encripta directamente la contraseña
        if commit:
            user.save()
        return user
    
class PersonaForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['is_userp']
        
    
