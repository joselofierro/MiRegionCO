# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0019_auto_20170825_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
