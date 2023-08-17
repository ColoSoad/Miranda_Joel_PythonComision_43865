from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # URLS PARA PÁGINA PRINCIPAL

    path('', index, name = 'inicio'),

#_______________________________________________________________#

   # URL PARA USUARIO CON CRUD 

    path('usuarios/', usuarios, name="usuarios"),
    path('usuario_form/', usuarioForm, name="usuario_form"),
    path('update_usuario/<id_usuario>/', updateUsuario, name="update_usuario" ),
    path('delete_usuario/<id_usuario>/', deleteUsuario, name="delete_usuario" ),
#_______________________________________________________________#

   # URL CON CRUD (CLASS BASED VIEWS)

# CLASE BASADA EN VISTA "LIST"
    path('pelicula/', PeliculaList.as_view(), name="pelicula"),
    path('serie/', SerieList.as_view(), name="serie"),
    path('documental/', DocumentalList.as_view(), name="documental"),

# CLASE BASADA EN VISTA "CREATE"
    path('create_pelicula/', PeliculaCreate.as_view(), name="create_pelicula"),
    path('create_serie/', SerieCreate.as_view(), name="create_serie"),
    path('create_documental/', DocumentalCreate.as_view(), name="create_documental"),

# CLASE BASADA EN VISTA "DETAIL"
    path('detail_pelicula/<int:pk>/', PeliculaDetail.as_view(), name='detail_pelicula'),
    path('detail_serie/<int:pk>/', SerieDetail.as_view(), name="detail_serie"),
    path('detail_documental/<int:pk>/', DocumentalDetail.as_view(), name="detail_documental"),

# CLASE BASADA EN VISTA "UPDATE"
    path('update_pelicula/<int:pk>/', PeliculaUpdate.as_view(), name="update_pelicula"),
    path('update_serie/<int:pk>/', SerieUpdate.as_view(), name="update_serie"),
    path('update_documental/<int:pk>/', DocumentalUpdate.as_view(), name="update_documental"),

# CLASE BASADA EN VISTA "DELETE"
    path('delete_pelicula/<int:pk>/', PeliculaDelete.as_view(), name="delete_pelicula"),
    path('delete_serie/<int:pk>/', SerieDelete.as_view(), name="delete_serie"),
    path('delete_documental/<int:pk>/', DocumentalDelete.as_view(), name="delete_documental"),

#_______________________________________________________________#

   # URLS PARA FORMULARIOS DE BÚSQUEDA Y RESULTADO (TIPO SEARCH)

    path('buscar_contenido/', buscarContenido, name="buscar_pelicula"),
    path('buscar2/', buscar2, name="buscar2"),

#_______________________________________________________________#

    # URL PARA SITIO PLATAFORMAS

    path('plataformas/', plataformas, name="plataformas"),

#_______________________________________________________________#

    # URL PARA SITIO "Acerca de mí"

    path('contactos/', contacto, name="contactos"),

#_______________________________________________________________#

    # URLS PARA LOGIN, LOGOUT Y REGISTRO

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registro/', register, name="registro"),

#_______________________________________________________________#

    # URLS PARA EDITAR PERFIL Y AVATAR

path('editar_perfil/', editarPerfil, name="editar_perfil"),

path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]