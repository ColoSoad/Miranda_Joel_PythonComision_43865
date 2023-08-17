from django.db import models
from django.contrib.auth.models import User
# Creamos nuestros modelos que van a representar todo el contenido y "Clientes" de nuestro sitio
# Con el método __str__ para obtener una mejor vista del lado del administrador.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.plataforma}"


class Serie(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.plataforma}"

class Documental(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.plataforma}"
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.email}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"