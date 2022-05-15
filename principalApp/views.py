from django.shortcuts import render
from publicacionesApp.models import Autor

def inicio(request):
    
    return render(request,'inicio/index.html')
