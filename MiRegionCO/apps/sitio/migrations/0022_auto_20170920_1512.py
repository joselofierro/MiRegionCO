# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0021_auto_20170918_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]