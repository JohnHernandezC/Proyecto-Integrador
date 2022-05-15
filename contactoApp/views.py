from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from django.core.mail import EmailMessage

def contacto(request):
    if request.method == 'POST':
        nombres=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

            
        emails=EmailMessage(" {} ".format(subject),"El usuario  {}\n Con el correo: {}\n Escribio:\n\n{}".format(nombres,email,message),
                               "",["aplicacionsalud1@gmail.com"],reply_to=[email])#lo ultimo es por si quieren colocar la opcion de responder
        try:
            emails.send()
            return redirect('/contactanos/contacto/?valido')
        except:
            return redirect('/contactanos/contacto/?novalido')
            
    return render(request,'contactos/contacto.html')  

def acerca(request):
    
    return render(request,'about/about.html')  
