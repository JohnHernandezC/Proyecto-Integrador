from rest_framework import serializers

from comentariosApp.models import Comentarios


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comentarios
        exclude=['autores','publicacion']