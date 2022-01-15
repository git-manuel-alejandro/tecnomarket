from contextlib import nullcontext
from pyexpat import model
from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to = 'procuctos' , null = True, )

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    consulta = models.CharField(max_length=20)

    def __str__(self):
        return self.consulta

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.ForeignKey(Consulta , on_delete=models.PROTECT)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


