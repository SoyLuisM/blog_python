from django.shortcuts import render
# from content_blog.models import catalogo_categorias as cat
from content_blog.models import post
from user_profile.models import profile

# Create your views here.
def home(request):
    """renderiza el home del sistema""" 
    posts = post.objects.all()
    try:
        posts = posts[::-1]
        posts = posts[0:8]
    except:
        pass
    print(post)
    return render(request,'home.html',{'posts':posts})

def autores(request):
    list_autores = profile.objects.all()
    return render(request,"autores.html",{'autores': list_autores})

def busqueda(request):
    if request.method == 'POST':
        print(request.POST['busqueda'])
        busqueda = post.objects.filter(titulo = request.POST['busqueda'])
        print(busqueda)
        if busqueda:
            print('encontré algo')
            return render(request, "busqueda.html",{'resultados': busqueda})
    
    print('no encontré nada')
    return render(request, "busqueda.html")

def m_puntuados(request):
    return render(request,"m_puntuados.html")

def leer_post(request,id_post):
    try:
        l_post = post.objects.get(id = id_post)
        return render(request,"leer_post.html",{'post':l_post})
    except:
        return render(request,"404.html")

def ver_post_autor(request,id_autor):
    post_user = post.objects.filter(autor=id_autor)
    return render(request,"ver_post_autores.html",{'posts':post_user})