"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from content_blog import views as content_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',content_views.home),
    path("autores",content_views.autores),
    path("busqueda",content_views.busqueda),
    path("login", content_views.login),
    path("registro", content_views.registro),
    path("recuperacion", content_views.recuperacion),
    path("mejor-puntuados", content_views.m_puntuados),
]
