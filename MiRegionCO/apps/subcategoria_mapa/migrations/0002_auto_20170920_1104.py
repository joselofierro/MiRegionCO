# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategoria_mapa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoriamapa',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]