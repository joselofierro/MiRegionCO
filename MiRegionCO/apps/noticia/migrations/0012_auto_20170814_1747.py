# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0011_auto_20170801_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='lead',
            field=models.CharField(max_length=220),
        ),
    ]
