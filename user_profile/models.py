from django.db import models
from django.contrib.auth.models import AbstractUser

class profile(AbstractUser):
    first_name = None
    last_name = None
    nombre = models.CharField(max_length=100,blank=True)
    a_paterno = models.CharField(max_length=100, blank=True)
    a_materno = models.CharField(max_length=100,blank=True)
    img = models.ImageField(upload_to = 'user/', max_length = 100, blank= True)