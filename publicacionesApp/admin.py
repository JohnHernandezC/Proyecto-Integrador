from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource (resources.ModelResource):
     class Meta:
         model = Categoria
         
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('nombre','estado')
    search_fields = ('nombre',)
    resources_class=CategoriaResource

class AutorAdmin(admin.ModelAdmin):
    list_display=('id','nickname')
    search_fields = ('id','nickname')
    
class ComentariosAdmin(admin.ModelAdmin):
    list_display=('id','calificacion')
    

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Comentarios,ComentariosAdmin)
admin.site.register(Post)
