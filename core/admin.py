from django.contrib import admin
from .models import Obra

class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado',  'created_at') # Lo que se ve en la lista
    list_filter = ('estado',) # Filtro lateral para ver solo vendidas/disponibles
    search_fields = ('titulo',) # Buscador

admin.site.register(Obra, ObraAdmin)