from django.contrib.auth import authenticate, login
from UsuariosApp.models import Usuario
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chatApp.models import Message
from chatApp.forms import SignUpForm
from chatApp.serializers import MessageSerializer






@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def chat_view(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        usuario=get_object_or_404(Usuario,pk=pk)
        return render(request, 'chat/chat.html',{'users': usuario, 'rece': pk})
        #return render(request, 'chat/chat.html',{'users': Usuario.objects.exclude(username=request.user.username )})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        print(sender)
        return redirect('login')
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': Usuario.objects.exclude(username=request.user.username),
                       'receiver': Usuario.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})
