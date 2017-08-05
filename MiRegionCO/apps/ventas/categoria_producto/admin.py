from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'medida',)


admin.site.register(CategoriaProducto, CategoriaAdmin)
