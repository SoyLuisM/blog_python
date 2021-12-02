from django import template
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import uuid

def send_mail(nombre,a_paterno,a_materno,mail):
    clave = uuid.uuid4

    #guardar clave en base de datos

    context = {
        'nombre' : nombre,
        'a_paterno' : a_paterno,
        'a_materno' : a_materno,
        'url': settings.DOMINIO,
        'clave': clave,
    }

    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'correo de prueba',
        'blog team 7',
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,'text/html')
    
    email.send()