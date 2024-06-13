from django.shortcuts import render, HttpResponse

def principal(request):
    return render(request, "cursosDjango/principal.html")

def cursos(request):
    return render(request, "cursosDjango/cursos.html")


def contacto(request):
    return render(request, "cursosDjango/contacto.html")
