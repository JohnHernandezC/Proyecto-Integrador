from django.db.models.signals import post_save
from .models import Usuario
from publicacionesApp.models import Autor
from django.dispatch import receiver

@receiver(post_save,sender=Usuario)
def create_autor(sender,instance,created, **kwargs):
    if created:
        Autor.objects.create(usuario=instance)