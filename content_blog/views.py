from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def autores(request):
    return render(request,"autores.html")

def busqueda(request):
    return render(request, "busqueda.html")

def login(request):
    return render(request, "login.html")

def recuperacion(request):
    return render(request, "recuperacion.html")

def registro(request):
    return render(request, "registro.html")

def m_puntuados(request):
    return render(request,"m_puntuados.html")