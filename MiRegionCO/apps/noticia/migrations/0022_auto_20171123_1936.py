# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0021_auto_20171123_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
