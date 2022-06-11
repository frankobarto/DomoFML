from django.contrib import admin
from gestionPersona.models import Personas, Propiedad,Evento

# Register your models here.
class PersonasAdmin(admin.ModelAdmin):
    list_display=("nombre_persona","nro_celular","correo_persona")
    search_fields=("nombre_persona","nro_celular")

admin.site.register(Personas, PersonasAdmin)
admin.site.register(Propiedad)
admin.site.register(Evento)