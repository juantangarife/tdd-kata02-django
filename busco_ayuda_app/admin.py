from django.contrib import admin

from .models import TiposDeServicio, Trabajador, Comentario


class TiposDeServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'trabajador')


class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos')


admin.site.register(TiposDeServicio, TiposDeServicioAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
