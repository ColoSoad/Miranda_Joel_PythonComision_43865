# FUNCION PARA CREAR NUEVAS "PELICULAS"
def peliculaForm(request):
    if request.method == "POST":   
        miForm = PeliculaForm(request.POST)
        if miForm.is_valid():
            pelicula_nombre = miForm.cleaned_data.get('nombre')
            pelicula_año = miForm.cleaned_data.get('año')
            pelicula_genero = miForm.cleaned_data.get('genero')
            pelicula_plataforma = miForm.cleaned_data.get('plataforma')
            pelicula = Pelicula(nombre=pelicula_nombre, año=pelicula_año, genero=pelicula_genero, plataforma=pelicula_plataforma)
            pelicula.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PeliculaForm()

    return render(request, "aplicacion/peliculaForm.html", {"form":miForm})

# FUNCION PARA CREAR NUEVAS "SERIES"
def serieForm(request):
    if request.method == "POST":   
        miForm = SerieForm(request.POST)
        if miForm.is_valid():
            serie_nombre = miForm.cleaned_data.get('nombre')
            serie_año = miForm.cleaned_data.get('año')
            serie_genero = miForm.cleaned_data.get('genero')
            serie_plataforma = miForm.cleaned_data.get('plataforma')
            serie = Serie(nombre=serie_nombre, año=serie_año, genero=serie_genero, plataforma=serie_plataforma)
            serie.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = SerieForm()

    return render(request, "aplicacion/serieForm.html", {"form":miForm})

# FUNCION PARA CREAR NUEVOS "DOCUMENTALES"
def documentalForm(request):
    if request.method == "POST":   
        miForm = DocumentalForm(request.POST)
        if miForm.is_valid():
            documental_nombre = miForm.cleaned_data.get('nombre')
            documental_año = miForm.cleaned_data.get('año')
            documental_genero = miForm.cleaned_data.get('genero')
            documental_plataforma = miForm.cleaned_data.get('plataforma')
            documental = Documental(nombre=documental_nombre, año=documental_año, genero=documental_genero, plataforma=documental_plataforma)
            documental.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DocumentalForm()

    return render(request, "aplicacion/documentalForm.html", {"form":miForm})


path('pelicula_form/', peliculaForm, name="peliculaForm"),
    path('serie_form/', serieForm, name="serieForm"),
    path('documental_form/', documentalForm, name="documentalForm"),








#_______________________________________________________________#

# CLASE BASADA EN VISTA PARA EL SITIO DE "PELICULAS"


class PeliculaList (ListView):
    model = Pelicula


# CLASE BASADA EN VISTA PARA EL SITIO DE "SERIES"

class SerieList (ListView):
    model = Serie



# CLASE BASADA EN VISTA PARA EL SITIO DE "DOCUMENTALES"

class DocumentalList (ListView):
    model = Documental



#_______________________________________________________________#

# CLASE BASADA EN VISTA  PARA CREAR NUEVAS "PELICULAS"

class PeliculaCreate(CreateView):
    model = Pelicula
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('pelicula')

# CLASE BASADA EN VISTA  PARA VER DETALLES DE "PELICULAS"

class PeliculaDetail (DetailView):
    model = Pelicula


# CLASE BASADA EN VISTA  PARA EDITAR "PELICULAS"

class PeliculaUpdate(UpdateView):
    model = Pelicula
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('pelicula')

# CLASE BASADA EN VISTA  PARA ELIMINAR "PELICULAS"

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula')

#_______________________________________________________________#

# CLASE BASADA EN VISTA  PARA CREAR NUEVAS "SERIES"

class SerieCreate(CreateView):
    model = Serie
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('serie')

# CLASE BASADA EN VISTA  PARA VER DETALLES DE "SERIES"

class SerieDetail (DetailView):
    model = Serie

# CLASE BASADA EN VISTA  PARA EDITAR "SERIES"

class SerieUpdate(UpdateView):
    model = Serie
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('serie')

# CLASE BASADA EN VISTA  PARA ELIMINAR "SERIES"

class SerieDelete(DeleteView):
    model = Serie
    success_url = reverse_lazy('serie')

#_______________________________________________________________#

# CLASE BASADA EN VISTA  PARA CREAR NUEVOS "DOCUMENTALES"

class DocumentalCreate(CreateView):
    model = Documental
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('documental')

# CLASE BASADA EN VISTA  PARA VER DETALLES DE "DOCUMENTALES"

class DocumentalDetail (DetailView):
    model = Documental

# CLASE BASADA EN VISTA  PARA EDITAR "DOCUMENTALES"

class DocumentalUpdate(UpdateView):
    model = Documental
    fields = ['nombre', 'año', 'genero', 'plataforma']
    success_url = reverse_lazy('documental')

# CLASE BASADA EN VISTA  PARA ELIMINAR "DOCUMENTALES"

class DocumentalDelete(DeleteView):
    model = Documental
    success_url = reverse_lazy('documental')




# update pelicula

def updatePelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    if request.method == "POST":
        miForm = PeliculaForm(request.POST)
        if miForm.is_valid():
            pelicula.nombre = miForm.cleaned_data.get('nombre')
            pelicula.año = miForm.cleaned_data.get('año')
            pelicula.genero = miForm.cleaned_data.get('genero')
            pelicula.plataforma = miForm.cleaned_data.get('plataforma')
            pelicula.save()
            return redirect(reverse_lazy, ("peliculas"))
    else:
        miForm = PeliculaForm(initial={'nombre':pelicula.nombre, 'año':pelicula.año, 'genero':pelicula.genero, 'plataforma':pelicula.plataforma})

    return render(request,"aplicas/peliculaForm.html", {'form': miForm})

#_______________________________________________________________#

    # FUNCION PARA CREAR NUEVAS "PELICULAS"
def peliculaForm(request):
    if request.method == "POST":   
        miForm = PeliculaForm(request.POST)
        if miForm.is_valid():
            pelicula_nombre = miForm.cleaned_data.get('nombre')
            pelicula_año = miForm.cleaned_data.get('año')
            pelicula_genero = miForm.cleaned_data.get('genero')
            pelicula_plataforma = miForm.cleaned_data.get('plataforma')
            pelicula = Pelicula(nombre=pelicula_nombre, año=pelicula_año, genero=pelicula_genero, plataforma=pelicula_plataforma)
            pelicula.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PeliculaForm()

    return render(request, "aplicacion/peliculaForm.html", {"form":miForm})

# FUNCION PARA EL SITIO DE "PELICULAS"
def peliculas(request):
    contexto = {"pelicula": Pelicula.objects.all() }
    return render(request, "aplicacion/pelicula.html", contexto)

path('peliculas/', peliculas, name="peliculas"),