"""ProyectoIntegrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('principalApp.urls','inicio'))),
    path('post/', include(('publicacionesApp.urls','blog'))),
    path('usuario/', include(('UsuariosApp.urls','usuarios'))),
    path('formulario/', include(('FormularioApp.urls','formularios'))),
    path('', include('pagosApp.urls')),
    path('comentarios/', include('comentariosApp.api.urls')),
    path('accounts/login/',LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('accounts/logout/',LogoutView.as_view(template_name='inicio/index.html'), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='autenticacion/password-reset.html'), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='autenticacion/reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='autenticacion/reset_Confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='autenticacion/reset_Complete.html'),name='password_reset_complete'),
    path('', include(('chatApp.urls','chats-index'))),
    
]



