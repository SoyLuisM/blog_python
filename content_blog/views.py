from django.shortcuts import render
from content_blog.models import catalogo_categorias as cat
from content_blog.models import post

# Create your views here.
def home(request):
    posts = post.objects.all().order_by('fecha_creacion')
    posts = posts[::-1]
    posts = posts[0:4]
    return render(request,'home.html',{'posts':posts})

def autores(request):
    return render(request,"autores.html")

def busqueda(request):
    return render(request, "busqueda.html")

def m_puntuados(request):
    return render(request,"m_puntuados.html")