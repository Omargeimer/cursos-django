from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
#Crear un modelo para administrar los cursos almacenando los datos que consideres necesarios "usa almenos 5 tipos de datos diferentes" (debes incluir una fecha de creación).

class Cursos(models.Model):#define la estructura de nuestra tabla
    nombre = models.TextField(verbose_name="Titulo del curso")#Texto largo
    carrera = models.TextField(verbose_name="Nombre Carrera")
    num_parciales = models.IntegerField(verbose_name="Número de Parciales")
    activo = models.BooleanField(default=True, verbose_name="¿Sigue Impartiendose?")
    web = models.URLField(verbose_name="Web para contenido")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado") #Fecha y tiempo

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla    


class Actividades(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")
    descripcion = RichTextField(verbose_name="Descripción de la actividad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name="Actividad"
        verbose_name_plural="Actividades"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self) -> str:
        return self.descripcion