from django.shortcuts import render
# from content_blog.models import catalogo_categorias as cat
from content_blog.models import post
from user_profile.models import profile

# Create your views here.
def home(request):
    """renderiza el home del sistema""" 
    posts = post.objects.all()
    # posts = posts[::-1]
    # posts = posts[0:4]
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