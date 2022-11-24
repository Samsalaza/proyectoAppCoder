from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso (request):
    curso=Curso(nombre="Curso Django", comision=1234455)
    curso.save()
    cadena_texto="Curso guardado: "+curso.nombre+ " "+str(curso.comision)
    return HttpResponse (cadena_texto)