from django import template
from django.templatetags.static import (static as _static)

register = template.Library()


def static(path):
    # Backwards compatibility alias for django.templatetags.static.static().
    # Deprecation should start in Django 2.0.
    return _static(path)


@register.filter
def escape_single_quotes(string):
    # The two backslashes are interpreted as a single one
    # because the backslash is the escaping character.
    return string.replace("'", "\\'")


@register.simple_tag
def update_variable(a, b):
    return a + b
