from django.shortcuts import render, HttpResponse
from cursos.models import Cursos


def principal(request):
    return render(request, "cursosDjango/principal.html")

def cursos(request):
    cursos=Cursos.objects.all()
    return render(request, "cursosDjango/cursos.html", {'cursos_list':cursos})


def contacto(request):
    return render(request, "cursosDjango/contacto.html")
