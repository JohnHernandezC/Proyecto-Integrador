from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name='general-post'),
    path('<int:id>/',detalles,name='detalles_post'),
    path('autor/<int:id>',autor,name='detalles-autor'),
    path('crear/',login_required(crearPost),name='crear-post'),
    path('listar/',login_required(listarMisPost),name='listar-post'),
    path('editar/<int:id>',login_required(editarPost),name='editar-post'),
    path('eliminar/<int:id>',login_required(eliminarPost),name='eliminar-post'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

