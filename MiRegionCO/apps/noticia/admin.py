from django.contrib import admin

# Register your models here.
from apps.noticia.models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_filter = ('categoria',)


admin.site.register(Noticia, NoticiaAdmin)
