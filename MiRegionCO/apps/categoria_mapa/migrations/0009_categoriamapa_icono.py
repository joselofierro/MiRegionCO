# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 23:37
from __future__ import unicode_literals

import apps.categoria_mapa.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_mapa', '0008_auto_20170901_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriamapa',
            name='icono',
            field=models.ImageField(default=1, upload_to=apps.categoria_mapa.models.upload_location_2),
            preserve_default=False,
        ),
    ]