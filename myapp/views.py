from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Organigrama,Persona,Dependencia
from .forms import crearNuevoOrganigrama,crearNuevaDependencia

# Create your views here.
def index(request): 
    title = "Welcome to django app!!"
    return render(request,'index.html',{
        'title':title
    })

def organigramas(request):
    organigramas = Organigrama.objects.all()
    return render(request,'organigrama.html',{
        'organigramas': organigramas
    }) 

def dependencias(request):
    dependencias = Dependencia.objects.all()
    return render(request,"dependencias.html",{
        'dependencias':dependencias
    })

def personas(request):
    personas = Persona.objects.all()
    return render(request,'personas.html',{
        'personas':personas
    })
def crear_organigrama(request):
    if request.method == "GET":
        return render(request,'crear_organigrama.html',{
        'form': crearNuevoOrganigrama()
        })
    else:
        Organigrama.objects.create(codigo_organigrama=request.POST['codigo_organigrama'],nombre_organigrama=request.POST['nombre_organigrama'])
        return redirect('organigramas')
    
def crear_dependencias(request):
    if request.method == "GET":
        return render(request,'crear_dependencias.html',{
            'form':crearNuevaDependencia()
        })
    else:
        Dependencia.objects.create(codigo_dependencia=request.POST["codigo_dependencia"],nombre_dependencia=request.POST["nombre_dependencia"],codigo_jefe=request.POST["codigo_jefe"])
        return redirect('organigramas')
