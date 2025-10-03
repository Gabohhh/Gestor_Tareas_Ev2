from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_creacion', 'fecha_limite')
    list_filter = ('vigente', 'prioridad', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_creacion'

    actions = ['marcar_como_inactivas']

    @admin.action(description="Marcar tareas seleccionadas como inactivas")
    def marcar_como_inactivas(self, request, queryset):
        updated = queryset.update(vigente=False)
        self.message_user(request, f"{updated} tareas marcadas como inactivas.")