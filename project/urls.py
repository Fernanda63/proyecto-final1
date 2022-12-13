"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ejemplo.views import (ActualizarAmigo, ActualizarCliente, AltaAmigo, BuscarAmigo, BuscarCliente, mostrar_Clientes, mostrar_Amigos, buscar, index, 
                            monstrar_familiares, BuscarFamiliar, 
                            AltaFamiliar, AltaCliente, ActualizarFamiliar, saludar_a, sumar) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), 
    path('saludar_a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>', sumar),
    path('buscar', buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mis-Amigos/', mostrar_Amigos),
    path('mis-Amigos/buscar', BuscarAmigo.as_view()),
    path('mis-Amigos/alta', AltaAmigo.as_view()),
    path('mis-Clientes/', mostrar_Clientes), 
    path('mis-Clientes/buscar', BuscarCliente.as_view()),
    path('mis-Clientes/alta', AltaCliente.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarAmigo.as_view()),
    path('mis-Clientes/actualizar/<int:pk>', ActualizarCliente.as_view()),
    ]


