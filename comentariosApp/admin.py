from django.contrib import admin
from comentariosApp.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


  
class ComentariosAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Comentarios,ComentariosAdmin)
