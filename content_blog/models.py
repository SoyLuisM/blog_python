from django.db import models
import uuid
# Create your models here.

class post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    contenido = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=100)


class categorias_post(models.Model):
    id_categorias = models.ForeignKey('catalogo_categorias',on_delete=models.CASCADE)
    id_post = models.ForeignKey('post',on_delete=models.CASCADE)


class catalogo_categorias(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=60)
    status = models.BooleanField(default=True)