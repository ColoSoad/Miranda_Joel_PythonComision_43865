from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# FORMULARIO PARA LA CREACION DE USUARIOS
class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre de Usuario", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido de Usuario", max_length=50, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)

# FORMULARIO PARA LA CREACION DE NUEVAS PELICULAS
class PeliculaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la película", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la película", required=True)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA CREACION DE NUEVAS SERIES
class SerieForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la serie", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la serie", required=True)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA CREACION DE NUEVOS DOCUMENTALES
class DocumentalForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la pelicula", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la pelicula", required=True)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

#FORMULARIO PARA EDITAR PELICULA

class PeliculaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la serie", max_length=50, required=True)
    año = forms.IntegerField(label= "Año de la serie", required=False)
    genero = forms.CharField(label="genero",max_length=50, required=True)
    plataforma = forms.CharField(label="plataforma",max_length=100, required=True)

# FORMULARIO PARA LA BUSQUEDA
class Busqueda(forms.Form):
    nombre = forms.CharField(label = "Buscar Contenido", max_length=30, required=True)

# FORMULARIO PARA REGISTRO DE USUARIOS (SUSTITUYENDO AL "UserCreationForm")
class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  # "HELP_ TEXTS" ELIMINA LOS MENSAJES DE AYUDA

# FORMULARIO PARA EDITAR PERFIL
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        help_texts = { k:"" for k in fields}  # "HELP_ TEXTS" ELIMINA LOS MENSAJES DE AYUDA

# FORMULARIO PARA AVATAR
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)   