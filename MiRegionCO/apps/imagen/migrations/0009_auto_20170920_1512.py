# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagen', '0008_auto_20170920_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(default='imagen', max_length=150),
        ),
    ]
