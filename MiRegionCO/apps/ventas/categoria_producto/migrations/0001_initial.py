# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('medida', models.CharField(max_length=50)),
            ],
        ),
    ]
