# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:00
from __future__ import unicode_literals

import apps.categoria_mapa.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_mapa', '0007_categoriamapa_icono_marcador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamapa',
            name='icono_marcador',
            field=models.ImageField(upload_to=apps.categoria_mapa.models.upload_location_2),
        ),
    ]
