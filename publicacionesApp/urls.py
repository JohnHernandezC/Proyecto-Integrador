from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name='general-post'),
    path('<int:id>/',login_required(detalles),name='detalles_post'),
    path('autor/<int:id>',autor,name='detalles-autor'),
    path('crear/',login_required(crearPost),name='crear-post'),
    path('listar/',login_required(listarMisPost),name='listar-post'),
    path('editar/<int:id>',login_required(editarPost),name='editar-post'),
    path('eliminar/<int:id>',login_required(eliminarPost),name='eliminar-post'),
    path('solicitar/<int:id>/<int:idA>',login_required(solicitudesP),name='solicitar-servicio'),
    path('listarSolicitudes/',login_required(controlMisPost),name='listar-Solicitudes'),
    path('aceptar/<int:id>',login_required(aceptarSolicitud),name='aceptar-solicitud'),
    path('denegar/<int:id>',login_required(denegarSolicitud),name='denegar-solicitud'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

