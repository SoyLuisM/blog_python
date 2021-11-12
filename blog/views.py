from django.http import HttpResponse

def hello_word(request):
    return HttpResponse('hola_mundo')