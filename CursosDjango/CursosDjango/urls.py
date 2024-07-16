from django.urls import path
from django.contrib import admin
from contenido import views as contenidoViews
from cursos import views as cursosViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contenidoViews.principal, name="Principal"),
    path('cursos/', contenidoViews.cursos, name="Cursos"),
    path('contacto/', contenidoViews.contacto, name="Contacto"),
    path('consulta1/', cursosViews.consultar1, name="Consulta1"),
    path('consulta2/', cursosViews.consultar2, name="Consulta2"),
    path('consulta3/', cursosViews.consultar3, name="Consulta3"),
    path('consulta4/', cursosViews.consultar4, name="Consulta4"),
    path('consulta5/', cursosViews.consultar5, name="Consulta5"),
    path('consulta6/', cursosViews.consultar6, name="Consulta6"),
]