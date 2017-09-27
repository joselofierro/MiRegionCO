from django.contrib import admin
from apps.usuario.models import Usuario


# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'idFacebook', 'nombreCompleto')
    list_filter = ('id', 'idFacebook', 'nombreCompleto')


admin.site.register(Usuario, UsuarioAdmin)
