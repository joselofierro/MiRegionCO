# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0023_auto_20170920_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
