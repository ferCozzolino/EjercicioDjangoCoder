from http.client import INSUFFICIENT_STORAGE
from multiprocessing import current_process
from django.urls import path
from .views import curso, cursos, entregables, estudiantes, inicio, lista_curso, profesores


urlpatterns = [

    path('agrega-curso/<nombre>/<camada>',curso),
    path('lista-cursos/',lista_curso),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('entregables/',entregables, name="Entregables"),
    path('cursos/',cursos, name="Cursos"),
    path('', inicio),    
   
]
