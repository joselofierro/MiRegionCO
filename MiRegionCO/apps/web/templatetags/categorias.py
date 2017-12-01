from django import template
from django.templatetags.static import (static as _static)
from apps.categoria.models import Categoria

register = template.Library()


def static(path):
    # Backwards compatibility alias for django.templatetags.static.static().
    # Deprecation should start in Django 2.0.
    return _static(path)


@register.inclusion_tag('base/categorias_menu.html', takes_context=True)
def categorias_menu(context):
    return {'categorias': Categoria.objects.filter(visibleWeb=True).order_by('orden')}
