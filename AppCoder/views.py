from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import cursoForm, profesoresForm
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

