from django.contrib import admin

# Register your models here.
from apps.imagen.models import Imagen


class ImagenAdmin(admin.ModelAdmin):
    list_filter = ('nombre',)


admin.site.register(Imagen, ImagenAdmin)
