from UsuariosApp.models import Usuario
from rest_framework import serializers
from chatApp.models import Message





class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Usuario.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Usuario.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
