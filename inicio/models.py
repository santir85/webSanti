from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seccion(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"

class Articulo(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="clasificacion_seccion")
    fecha_publicacion = models.DateField(null= False)
    titulo = models.CharField(max_length=250, null=False)
    precio = models.FloatField()
    contenido = models.CharField(max_length=2000, null=False)
    imagen = models.FileField(upload_to='imagenes/')
    
    publicador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publicador")

    def __str__(self):
        return f"{self.fecha_publicacion} - {self.titulo} ({self.publicador})"

class LeerMasTarde(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    publicaciones = models.ManyToManyField(Articulo)

    def __str__(self):
        return f"{self.usuario} - {self.publicaciones}"