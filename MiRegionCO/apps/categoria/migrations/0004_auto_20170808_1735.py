# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_auto_20170724_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='azul',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='rojo',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='verde',
        ),
    ]