# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_remove_sitio_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitio',
            name='imagenes',
        ),
    ]
