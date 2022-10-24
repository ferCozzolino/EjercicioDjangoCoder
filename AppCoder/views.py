from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(request, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
    """)

def lista_curso(request):
    lista = Curso.objects.all()
    return render(request, "lista_cursos.html", {"lista_cursos": lista})
