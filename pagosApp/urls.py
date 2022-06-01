
from django.conf.urls.static import static

from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('pago/',login_required(pago),name='pago')
]