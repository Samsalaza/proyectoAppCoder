from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import cursoForm, profesoresForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView 
from django.urls import reverse_lazy
# Create your views here.

def curso (request):
    curso=Curso(nombre="Curso Django", comision=1234455)
    curso.save()
    cadena_texto="Curso guardado: "+curso.nombre+ " "+str(curso.comision)
    return HttpResponse (cadena_texto)

def inicio (request):
    return render (request, "AppCoder/inicio.html")

def cursos (request):
    return render (request, "AppCoder/cursos.html")

def estudiantes (request):
    return render (request, "AppCoder/estudiantes.html")

def entregables (request):
    return render (request, "AppCoder/entregables.html")

def profesores (request):
     if request.method=="POST":
        form=profesoresForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesiones=info["profesiones"]

            profe_Form=Profesor(nombre=nombre, apellido=apellido, email=email, profesiones=profesiones)
            profe_Form.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Profesor creado correctamente"})
     else:
        formulario=profesoresForm

        return render (request, "AppCoder/profesores.html", {"form": formulario})
   

def cursoFormulario(request):

    if request.method=="POST":
        form=cursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombrecito=info["nombre"]
            comisioncita=info["comision"]

            curso_Form=Curso(nombre=nombrecito, comision=comisioncita)
            curso_Form.save()
            return render (request, "AppCoder/inicio.html")

    else:
        formulario=cursoForm

    return render (request, "AppCoder/cursoFormulario.html", {"form": formulario})


def busquedaComision (request):
        return render(request, "AppCoder/busquedaComision.html")


def buscar (request):

    if request.GET["comision"]:
        comision=request.GET["comision"]
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppCoder/resultadoBusqueda.html",{"cursos":cursos})
    else:
        return render ("AppCoder/busquedaComision.html",{"mensaje":"INGRESA UNA COMISION!"})

def leerProfesores (request):
    profesores=Profesor.objects.all()
    return render (request, "AppCoder/leerProfesores.html",{"profesores":profesores})

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render (request, "AppCoder/leerProfesores.html", {"mensaje": "El profesor ha sido borrado correctmente!", "profesores": profesores})

def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=profesoresForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.email=informacion["email"]
            profesor.profesiones=informacion["profesiones"]
            profesor.save()
            profesores=Profesor.objects.all()
        return render(request,  "AppCoder/leerProfesores.html", {"mensaje": "El profesor ha sido editado correctmente!", "profesores":profesores})
    else:
        formulario=profesoresForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesiones":profesor.profesiones})
    return render (request, "AppCoder/editarProfesores.html", {"form": formulario, "profesor": profesor})


    #vistas basadas en clases

class EstudianteList (ListView):
    model=Estudiantes
    template_name= "AppCoder/leerEstudiantes.html"

class EstudianteCreacion (CreateView):
    model=Estudiantes
    success_url=reverse_lazy("estudiante_listar")
    fields=["nombre", "apellido", "email"]

class EstudianteUpdate (UpdateView):
    model=Estudiantes
    success_url=reverse_lazy("estudiante_listar")
    fields=["nombre", "apellido", "email"]

class EstudianteDelete (DeleteView):
    model=Estudiantes
    success_url=reverse_lazy("estudiante_listar")

class EstudianteDetalle (DetailView):
    model=Estudiantes
    template_name="AppCoder/estudiantes_detalle.html"
