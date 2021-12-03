from user_profile.models import profile as user

def datos_completos(data):
    for valor in data.values():
        if not valor:
            return False
    return True

def validar_email(valor):
    if user.objects.filter(email=valor):
        return True
    else:
        return False

def validar_nickname(valor):
    if not user.objects.filter(username=valor):
        return True
    else:
        return False

# def is_complete(clave):
#     res = user.objects.filter(clave_confirmacion=clave)
#     return res.is_active