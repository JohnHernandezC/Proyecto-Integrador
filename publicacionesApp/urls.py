from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='general-post'),
    path('<int:id>/',detalles,name='detalles_post'),
    path('autor/<int:id>',autor,name='detalles-autor'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
