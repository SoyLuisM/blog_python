from django.shortcuts import redirect, render
from user_profile.send_email import send_mail
from user_profile import querys
from user_profile import utilities
import uuid
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_user
from django.contrib.auth.decorators import login_required
from content_blog.models import post as post_models
from content_blog.models import catalogo_categorias as cat

@login_required
def logout_user(request):
    print('hola')
    logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username, password = password)
        if user is not None:
            print('ok')
            login_user(request, user)
            return redirect('/')
        else:
            return render(request, "login.html",{'error':'algo salio mal'})
    
    return render(request, "login.html")

def recuperacion(request):
    return render(request, "recuperacion.html")

def confirmacion(request,id):
    if request.method == 'POST':
        data = {
            'email' : request.POST['email'],
            'nickname' : request.POST['nickname'],
            'password' : request.POST['password'],
            'genero' : request.POST['genero'],
            'id' : id,
        }
        # if utilities.is_complete(id):
        #     render(request,"mensaje_display.html",{'succes':'Ya validaste tu cuenta'})
        if utilities.datos_completos(data):
            if utilities.validar_email(data['email']):
                print('email valido')
            else:
                return render(request, "confirmacion.html",{
                    'id':id,
                    'error':'email no valido',
                })

            if utilities.validar_nickname(data['nickname']):
                print('nickname valido')
            else:
                return render(request, "confirmacion.html",{
                    'id':id,
                    'error':'nickname en uso',
                })
            querys.confirm_user(data)
            return redirect('/')

        else:
            return render(request, "confirmacion.html",{
                'id':id,
                'error':'datos incompletos',
            })

    #se debe registrar en la base de datos la confirmacion
    #si el id es valido pero ya se actualizaron los datos se debe notificar 
    return render(request, "confirmacion.html",{'id':id,})

def registro(request):
    if request.method == 'POST':
        data = {
            'email' : request.POST['email'],
            'nombre' : request.POST['nombre'],
            'a_paterno' : request.POST['a_paterno'],
            'a_materno' : request.POST['a_materno'],
        }
        if utilities.datos_completos(data):
            clave = uuid.uuid4()
            #se deben limpiar los datos antes de  ingresar a la bd
            new_user = querys.create_user(data['email'],data['nombre'],data['a_paterno'],data['a_materno'],clave)

            if new_user:
                send_mail(data['nombre'],data['a_paterno'],data['a_materno'],data['email'],clave) 
                return render(request, "registro.html",{'succes':'se envio un email de confirmación'})
            else:
                return render(request, "registro.html",{'error':'El Correo ingresado ya esta registrado'})
            
            
        else:
            return render(request, "registro.html",{'error':'datos incompletos'})

    return render(request, "registro.html")

@login_required
def profile_user(request,user):
    return render(request,"user_profile_home.html")

@login_required
def create_post(request,user,action):
    # profile = request.user.a_paterno
    # print(profile)
    if request.method == 'POST':
        categorias = cat.objects.all()
        # print(request.POST['img'])
        try:
            
            datos = {
            'titulo' : request.POST['titulo'],
            # 'img' : request.POST['img'],
            'categorias' : request.POST['categorias'],
            'contenido' : request.POST['contenido'],
            # 'usuario' : request.user.username,
            }
            if utilities.datos_completos(datos):
                new_post= post_models(
                    titulo = datos['titulo'],
                    contenido = datos['contenido'],
                    img = request.FILES['img'],
                    status = True,
                    autor = request.user
                )
                post_cat = cat.objects.get(nombre = request.POST['categorias'])
                print(post_cat.nombre)
                new_post.save()
                post_cat.categorias.add(new_post)
                return redirect('/')
            else:
                raise('datos incompletos')
        except:
            return render(request,"user_profile_create_post.html",{
                'categorias':categorias,
                'error': "datos incompletos"
            })
        

    if not action:
        return render(request,"user_profile.html")
    
    if action == 'crearpost':
        categorias = cat.objects.all()
        return render(request,"user_profile_create_post.html",{'categorias':categorias})
    elif action == "update":
        return render(request,"user_profile_actualizar_datos.html")
    elif action == "mispost":
        return render(request,"user_profile_mis_post.html")
    else:
        return render(request,"404.html")
    

    