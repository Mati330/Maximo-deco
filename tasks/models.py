from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Referentes_soporte(models.Model):
    
    imagen_error_soporteuno = CloudinaryField(null=True, blank=True)
    imagen_error_soportedos = CloudinaryField(null=True, blank=True)
    imagen_error_soportetres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'
    
    
    
class Referentes_desarrollo(models.Model):
    
    imagen_error_desarrollouno = CloudinaryField(null=True, blank=True)
    imagen_error_desarrollodos = CloudinaryField(null=True, blank=True)
    imagen_error_desarrollotres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'
    
class Referentes_swbase(models.Model):
    
    imagen_error_swbaseuno = CloudinaryField(null=True, blank=True)
    imagen_error_swbasedos = CloudinaryField(null=True, blank=True)
    imagen_error_swbasetres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'

class Referentes_redes(models.Model):
    
    imagen_error_redesuno = CloudinaryField(null=True, blank=True)
    imagen_error_redesdos = CloudinaryField(null=True, blank=True)
    imagen_error_redestres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'
    
class Referentes_tel(models.Model):
    
    imagen_error_teluno = CloudinaryField(null=True, blank=True)
    imagen_error_teldos = CloudinaryField(null=True, blank=True)
    imagen_error_teltres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'
    
class Referentes_seginf(models.Model):
    
    imagen_error_seginfuno = CloudinaryField(null=True, blank=True)
    imagen_error_seginfdos = CloudinaryField(null=True, blank=True)
    imagen_error_seginftres =CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'


class Formularios(models.Model):
    
    imagen_error_formulariouno = CloudinaryField(null=True, blank=True)
    imagen_error_formulariodos = CloudinaryField(null=True, blank=True)
    imagen_error_formulariotres = CloudinaryField(null=True, blank=True)
    area_principal = models.CharField(max_length=50,null=True)
    nombre_referente= models.CharField(max_length=50,null=True)
    nombres_integrantes= models.CharField(max_length=60,null=True)
    apps = models.CharField(max_length=500,null=True)
    
    titulo_error = models.CharField(max_length=50,null=True)
    descripcion_error = RichTextField(blank=True, null=True)
    fecha_error= models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titulo_error}'

 
#class Errores_pedidos(models.Model):
 #   imagen = models.ImageField(null=True, blank=True)
  #  titulo = models.CharField(max_length=50,null=True)
   # descripcion = RichTextField(blank=True, null=True)
   # fecha= models.DateField()
   # autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
   # referente = models.ForeignKey(Referentes_soporte,Referentes_desarrollo, null=True, blank=True)
    
    #def __str__(self):
     #   return f'{self.titulo}'


