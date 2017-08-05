from django.contrib import admin

# Register your models here.
from apps.tag.models import Tag

admin.site.register(Tag)
