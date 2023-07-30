from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('instructores/', instructores, name="instructores"),
    path('alumnos/', alumnos, name="alumnos"),
    path('clases/', clases, name="clases"),
    path('entregables/', entregables, name="entregables"),

    path('clase_form/', claseForm, name="clase_form"),
    path('clase_form2/', claseForm2, name="clase_form2"),

    path('buscar_Codigo/', buscarCodigo, name="buscar_Codigo"),
    path('buscar2/', buscar2, name="buscar2"),
]