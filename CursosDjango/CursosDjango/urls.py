from django.urls import path
from contenido import views as contenidoViews

urlpatterns = [
    path('', contenidoViews.principal, name="Principal"),
    path('cursos/', contenidoViews.cursos, name="Cursos"),
    path('contacto/', contenidoViews.contacto, name="Contacto"),
]