from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#_______________________________________________________________#

# FUNCION PARA RENDERIZAR LA PAGINA PRINCIPAL

def index(request):
    return render(request, 'aplicacion/base.html')

#_______________________________________________________________#

   # FUNCION PARA EL SITIO USUARIO CON CRUD 

@login_required
def usuarios(request):
    contexto = {"usuario": Usuario.objects.all() }                  
    return render(request, "aplicacion/usuario.html", contexto)

    # FUNCION CRUD PARA CREAR NUEVOS USUARIOS

@login_required
def usuarioForm(request):
    if request.method == "POST":   
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get('nombre')
            usuario_apellido = miForm.cleaned_data.get('apellido')
            usuario_email = miForm.cleaned_data.get('email')
            usuario = Usuario(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email)
            usuario.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = UsuarioForm()

    return render(request, "aplicacion/usuarioForm.html", {"form":miForm})

    # FUNCION PARA EDITAR USUARIOS

@login_required
def updateUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario.nombre = miForm.cleaned_data.get('nombre')
            usuario.apellido = miForm.cleaned_data.get('apellido')
            usuario.email = miForm.cleaned_data.get('email')
            usuario.save()
            return redirect(reverse_lazy('usuarios'))
    else:
        miForm = UsuarioForm(initial={
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'email': usuario.email,
        })
    return render(request, "aplicacion/usuarioForm.html", {'form': miForm})

    # FUNCION PARA ELIMINAR USUARIOS

@login_required
def deleteUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect(reverse_lazy('usuarios'))

#_______________________________________________________________#

    # VIEWS CON CRUD (CLASS BASED VIEWS)

# CLASE BASADA EN VISTA "LIST"
class PeliculaList(LoginRequiredMixin, ListView):
    model = Pelicula
class SerieList(LoginRequiredMixin, ListView):
    model = Serie
class DocumentalList(LoginRequiredMixin, ListView):
    model = Documental

# CLASE BASADA EN VISTA "CREATE"
class PeliculaCreate(LoginRequiredMixin, CreateView):
    model = Pelicula
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('pelicula')
class SerieCreate(LoginRequiredMixin, CreateView):
    model = Serie
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('serie')
class DocumentalCreate(LoginRequiredMixin, CreateView):
    model = Documental
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('documental')

# CLASE BASADA EN VISTA "DETAIL"
class PeliculaDetail (LoginRequiredMixin, DetailView):
    model = Pelicula
class SerieDetail (LoginRequiredMixin, DetailView):
    model = Serie
class DocumentalDetail (LoginRequiredMixin, DetailView):
    model = Documental

# CLASE BASADA EN VISTA "UPDATE"
class PeliculaUpdate(LoginRequiredMixin, UpdateView):
    model = Pelicula
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('pelicula')
class SerieUpdate(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('serie')
class DocumentalUpdate(LoginRequiredMixin, UpdateView):
    model = Documental
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('documental')

# CLASE BASADA EN VISTA "DELETE"
class PeliculaDelete(LoginRequiredMixin, DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula')
class SerieDelete(LoginRequiredMixin, DeleteView):
    model = Serie
    success_url = reverse_lazy('serie')
class DocumentalDelete(LoginRequiredMixin, DeleteView):
    model = Documental
    success_url = reverse_lazy('documental') 

#_______________________________________________________________#

# FUNCION PARA BUSCAR CONTENIDO
@login_required
def buscarContenido(request):
    return render(request, "aplicacion/buscarContenido.html")


# FUNCION PARA DEVOLVER EL RESULTADO DE LA BUSQUEDA DE "CONTENIDO"
@login_required
def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        resultado_peliculas = Pelicula.objects.filter(nombre__icontains=nombre)
        resultado_documentales = Documental.objects.filter(nombre__icontains=nombre)
        resultado_series = Serie.objects.filter(nombre__icontains=nombre)
        if resultado_peliculas:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados":resultado_peliculas})
        elif resultado_documentales:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados": resultado_documentales})
        elif resultado_series:
            return render(request, "aplicacion/resultadosPelicula.html", {"nombre": nombre, "resultados": resultado_series})
        else:
            return render(request, "aplicacion/respuesta.html")
    else:
        return render(request, "aplicacion/base.html")

#_______________________________________________________________#

# FUNCION PARA EL SITIO DE "PLATAFORMAS"

def plataformas(request):
    return render(request, 'aplicacion/plataformas.html')


# FUNCION PARA EL SITIO DE "Acerca de Mí"
def contacto(request):
    return render(request, 'aplicacion/acercaDeMi.html')

#_______________________________________________________________#

# FUNCIONES PARA LOGIN, LOGOUT Y REGISTRO

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)  
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": form})

#_______________________________________________________________#

    # FUNCION PARA EDITAR PERFIL

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})

#_______________________________________________________________#

    #FUNCION PARA AGREGAR AVATAR

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})