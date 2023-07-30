from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from .models import Clases

def index(request):
    return render(request, "aplicacion/base.html")

def instructores(request):
    return render(request, "aplicacion/instructores.html")

def alumnos(request):
    return render(request, "aplicacion/alumnos.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")

def clases(request):
    ctx = {"clases": Clases.objects.all()}  
    return render(request, "aplicacion/clases.html", ctx)

def claseForm(request):
    if request.method == 'POST':
        clase= Clases (nombre=request.POST['nombre'], codigo=request.POST['codigo'],)
        clase.save()
        return HttpResponse('Se grabo con exito el curso!')
    
    return render(request, 'aplicacion/claseForm.html')


def claseForm2(request):
    if request.method == "POST":   
        miForm = ClaseForm(request.POST)
        if miForm.is_valid():
            clase_nombre = miForm.cleaned_data.get('nombre')
            clase_codigo = miForm.cleaned_data.get('codigo') 
            clase = Clases(nombre=clase_nombre, codigo=clase_codigo)  
            clase.save()
            return render(request, "aplicacion/claseform2.html", {'form': miForm})
    else:
        miForm = ClaseForm()

    return render(request, "aplicacion/claseForm2.html", {"form": miForm})

def buscarCodigo(request):
    return render(request, "aplicacion/buscarCodigo.html")

def buscar2(request):
    if request.GET['codigo']:  
        codigo = request.GET['codigo']  
        clases = Clases.objects.filter(codigo__icontains=codigo)  
        return render(request, 
                      "aplicacion/resultadosCodigo.html", 
                      {"codigo": codigo, "clases": clases}) 
    return HttpResponse("No se ingresaron datos para buscar!")


