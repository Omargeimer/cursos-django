from django.shortcuts import render
from .models import Cursos
from .models import Actividades
import datetime


def consultar1(request):
    #Consultando entre modelos
    actividades_filtradas=Actividades.objects.filter(curso__nombre__exact='Matemáticas')
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})

def consultar2(request):
    #Consultando entre modelos
    actividades_filtradas=Actividades.objects.filter(curso__nombre__iexact='matemáticas')
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})

def consultar3(request):
    #Consultando entre modelos
    actividades_filtradas=Actividades.objects.filter(curso__nombre__endswith='s')
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})

def consultar4(request):
    #Consultando entre modelos
    actividades_filtradas=Actividades.objects.filter(curso__nombre__startswith='P')
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})

def consultar5(request):
    #Consultando entre modelos
    fecha = datetime.date(2024, 6, 1)
    actividades_filtradas=Actividades.objects.filter(curso__created__gte=fecha)
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})

def consultar6(request):
    #Consultando entre modelos
    fecha = datetime.date(2024, 7, 1)
    actividades_filtradas=Actividades.objects.filter(curso__created__lt=fecha)
    return render(request,"CursosDjango/consultas.html",{'act_list':actividades_filtradas})