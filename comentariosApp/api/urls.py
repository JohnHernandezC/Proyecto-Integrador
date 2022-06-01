from django.contrib import admin
from django.urls import path

from comentariosApp.api.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('comentarioc/<int:pk>/<int:pk2>', login_required(ComentarioCreate.as_view()),name='comentario-create'),
    path('comentariol/<int:pk>', ComentarioLis.as_view(),name='comentario-list'),#tae la lista de comentarios pertenecientes a un autor
    path('comentario/<int:pk>', ComentariosDetail.as_view(),name='comentario-detail'),
]