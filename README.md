# Proyecto Final - Coder House - Python


# Alumno: Miranda, Joel Hernán
# Comisión: 43865
# SUPERUSUARIO: pythoncoderdjango
# PASSWORD: 3650coder


# Versión
1.1

# Tecnología
Front-End utilizado
- HTML 5
- CSS 3
- Bootstrap


Back-End utilizado
- Python 3.11
- Django version 4.2.3

# Descripción

Sitio Web con posibilidad de ser app multiplataforma para smartv, smartphone, pc, android, apple.
La idea principal es una app que evite el "zapping" entre plataformas de contenido, adaptandose a las base de datos de las 
plataformas  que se quiera, luego registrar el usuario. Buscar el contenido que quieras y que la app informe en que plataforma 
se encuentra dicho contenido. También ofrece un apartado donde se puede suscribir a las plataformas de streaming.

La app tiene posibilidades de evolucionar en varias formas y adaptarse a nuevas tecnologías.
El proyecto contiene comentarios por todos los apartados para poder entender bien.

La opción para crear nuevos usuarios es el "botton" "REGISTRATE!" en las demás opciones para agregar contenido, es en la misma tabla
donde aparece el contenido asociado, por ejemplo, si estamos en "Series": arriba de todo el contenido de series 
hay un boton "SERIES +" el cual se encarga de redireccionar para que presente el formulario.
Para los formularios de "usuarios" utilice funciones CRUD para poder aprender bien la lógica del procedimiento, para los demás modelos
utilice CRUD class based views.
En el pie del sitio está el apartado "Acerca de Mí" y dentro hay una leyenda describiendome, mi dirección, correo, celular y mis redes sociales.

# Objetivos

1. Un diseño / templates no usados en la clase, con un menú que tenga 
mínimamente 4 links (opciones de menú) //// El diseño es de "startbootstrap" - "grayscale" y contiene 9 links, "USUARIOS, PELICULAS, SERIES, DOCUMENTALES, PLATAFORMAS, SALIR, ACERCA DE MI, EL NOMBRE DE USUARIO QUE LO USE COMO LINK PARA EDITAR PERFIL Y LA BARRA DE BUSQUEDA" 

2. Login / Logout / Registro / Modificación de Usuarios (incluyendo un avatar o
foto del usuario logueado) //// El botón "Login" esta representado por "Iniciar Sesión". Logout por "SALIR". Registro por "REGISTRATE". Modificación de Usuarios se puede modificar desde "Editar perfil" incluyendo el avatar o desde la lista de usuarios con la funcionalidad crud.

3. Funcionalidad de CRUD en la aplicación de al menos 4 modelos, con sus
correspondientes formularios, habilitados solo para usuarios logueados //// Para los formularios de "usuarios" utilice funciones CRUD para poder aprender bien la lógica del procedimiento. Para los demás modelos (Pelicula, Serie, Documental) utilice CRUD class based views.
Si el usuario no se encuentra logueado ó registrado, sólo tiene la posibilidad de visualizar, "REGISTRATE, ADMINISTRACION, PLATAFORMAS, INICIAR SESION, ACERCA DE MI". Y una vez logueado, tiene acceso a todo lo demás y a la barra de búsqueda.

4. Un link a una página Acerca de mí, que cuente con datos del alumno //// En el pie del sitio se encuetra el apartado "Acerca de Mí" y dentro hay una leyenda describiendome, mi dirección, correo, celular y mis redes sociales.

5. Un search que se use como filtro de la información a mostrar (opcional) //// El sitio cuenta con un sercha que funciona de la sig manera:
A) Si no se busca nada, se queda en el mismo sitio.
B) Si se ingresa una letra o un un grupo de letras sin formar una palabra, busca por patrón de coincidencias.
C) Si se ingresa algun título del contenido en la base de datos, se redirecciona al archivo y lo muestra los detalles, lo mas importante y el objetivo principal de éste sitio, muestra en que plataforma se encuetra dicho contenido.
D) Si lo ingresado no se encuentra ni coincide con ningún patrón, informa que lo ingresado no es válido.


#   M i r a n d a _ J o e l _ C o m i s i o n _ 4 3 8 6 5  
 