# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0020_auto_20170828_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='descripcion',
            field=models.TextField(),
        ),
    ]