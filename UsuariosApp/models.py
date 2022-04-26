from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin       

from django.contrib.contenttypes.models import ContentType     

class Rol(models.Model):
   
    id = models.AutoField(primary_key = True)
    rol = models.CharField('Rol', max_length=50,unique = True)

    class Meta:
        

        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

    def __str__(self):
        
        return self.rol
    
    
        


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electronico")
            #genera un error si no pasamos un correo de
            
            #el self.model hace referencia directa a el modelo que estamos usando
        usuario=self.model(username=username,
                           email=self.normalize_email(email),
                           nombres=nombres,
                           apellidos=apellidos)
        usuario.set_password(password)#se usa la incriptacion de django que esta definido en el abstract
        usuario.save()
        return usuario
    def create_superuser(self,email,username,nombres,apellidos,password):
        usuario=self.create_user(
                    email,
                    username=username,
                    nombres=nombres,
                    apellidos=apellidos,
                    password=password  
        )
        usuario.usuario_admin=True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True)
    imagen = models.ImageField('Imagen de Perfil', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    usuario_admin  = models.BooleanField(default = False)
  
    objects = UsuarioManager()

    USERNAME_FIELD='username' #hace referencia al parametro unico puede ser esto o el coreo
    REQUIRED_FIELDS=['email','nombres','apellidos']#campos requeridos al momento de crear por consola
    
    
    def __str__(self):
        return self.nombres
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_admin   


    
