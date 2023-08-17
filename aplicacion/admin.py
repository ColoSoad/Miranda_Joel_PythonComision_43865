# Éste archivo "admin.py" nos permite configurar el Panel de administración

from django.contrib import admin

# Primero importamos los modelos (class)

from .models import * 

# Luego registramos los modelos:

admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Documental)
admin.site.register(Usuario)
admin.site.register(Avatar)

# Con ésto tenemos acceso a todo el material de la página web, osea, "peliculas, series, documentales y usuarios", lo importante
# que veo es que en un futuro cuando la página esté en la red con "clientes", se va a poder administrar sin la necesidad de acceder 
# a la base de datos mediante "dbBrowser" ó visual studio, ya que va a estar habilitado desde cualquier ordenador por el lado de 
# "ADMINISTRADOR". Segun el usuario que la manipule, los permisos que tenga asignados el mismo.