from django.contrib import admin
from .models import Cursos
from .models import Actividades


# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_field = ('created')
    list_display = ('nombre', 'carrera','num_parciales', 'created')
    search_fields = ('nombre', 'carrera','num_parciales')
    date_hierarchy = 'created'
    list_filter = ('carrera','num_parciales')


admin.site.register(Cursos, AdministrarModelo)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ("id", 'descripcion')
    search_fields = ("id", 'created')
    date_hierarchy = 'created'
    readonly_fields = ('id', 'created')
    list_display_links=('id','descripcion')

admin.site.register(Actividades, AdministrarActividades)