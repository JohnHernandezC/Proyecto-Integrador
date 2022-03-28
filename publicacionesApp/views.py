from django.shortcuts import render
from .models import *

def home (request):
    post=Post.objects.filter(estado=True)
    return render(request,'publications\publicaciones.html',{'post':post})
