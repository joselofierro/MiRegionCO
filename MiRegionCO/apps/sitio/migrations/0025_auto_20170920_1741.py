# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 22:41
from __future__ import unicode_literals

import apps.sitio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0024_auto_20170920_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.sitio.models.upload_location),
        ),
    ]