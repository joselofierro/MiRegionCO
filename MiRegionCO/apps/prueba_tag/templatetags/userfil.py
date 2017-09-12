from django import template
from django.contrib.auth.models import Group
from django.templatetags.static import (do_static as _do_static, static as _static)

register = template.Library()


def static(path):
    # Backwards compatibility alias for django.templatetags.static.static().
    # Deprecation should start in Django 2.0.
    return _static(path)


@register.filter(name='has_group')
def has_group(user, group_name):
    # obtengo el nombre del grupo
    group = Group.objects.get(name=group_name)
    # retorno el grupo en todos los grupos del usuario
    return group in user.groups.all()
