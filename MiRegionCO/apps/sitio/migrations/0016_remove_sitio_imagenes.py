# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0015_auto_20170816_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitio',
            name='imagenes',
        ),
    ]
