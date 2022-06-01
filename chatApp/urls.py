from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    path('chat/<int:pk>', login_required(chat_view), name='chats'),
    path('chat/<int:sender>/<int:receiver>/', login_required(message_view), name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', login_required(message_list), name='message-detail'),
    path('api/messages/', login_required(message_list), name='message-list'),
    
]
