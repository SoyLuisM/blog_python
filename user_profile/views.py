from django.shortcuts import render
from user_profile.send_email import send_mail
# Create your views here.
def login(request):
    return render(request, "login.html")

def recuperacion(request):
    return render(request, "recuperacion.html")

def confirmacion(request,id):
    #debe aceptar el metodo post
    #se debe registrar en la base de datos la confirmacion
    #si el id es valido pero ya se actualizaron los datos se debe notificar 
    return render(request, "confirmacion.html",{'id':id})

def registro(request):
    if request.method == 'POST':
        data = {
            'email' : request.POST['email'],
            'nombre' : request.POST['nombre'],
            'a_paterno' : request.POST['a_paterno'],
            'a_materno' : request.POST['a_materno'],
        }
        if(data['nombre'] and data['email'] and data['a_paterno'] and data['a_materno']):
            #si email existe en la base de datos
                #return render(request, "registro.html",{'error':'el correo ya existe'})

            #se deben limpiar los datos antes de  ingresar a la bd
            # se deben guardar los datos en la base de datos
            send_mail(data['nombre'],data['a_paterno'],data['a_materno'],data['email'])    
            return render(request, "registro.html",{'succes':'se envio un email de confirmación'})
        else:
            return render(request, "registro.html",{'error':'datos incompletos'})

    return render(request, "registro.html")