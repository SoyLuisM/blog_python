from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def recuperacion(request):
    return render(request, "recuperacion.html")

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
            # se debe enviar el email de confirmación    
            return render(request, "registro.html",{'succes':'se envio un email de confirmación'})
        else:
            return render(request, "registro.html",{'error':'datos incompletos'})

    return render(request, "registro.html")