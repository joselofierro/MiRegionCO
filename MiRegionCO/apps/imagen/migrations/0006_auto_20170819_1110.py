# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagen', '0005_auto_20170818_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
