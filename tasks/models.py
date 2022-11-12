from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Product(models.Model):
    imagen_product = models.ImageField(upload_to='product/')
    titulo = models.CharField(max_length=50)
    descripcion = models.SlugField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.titulo}'

class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')
    
    def __str__(self):
        return f'{self.logo}'
