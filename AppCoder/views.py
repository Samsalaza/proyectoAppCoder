from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
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
    return render (request, "AppCoder/profesores.html")