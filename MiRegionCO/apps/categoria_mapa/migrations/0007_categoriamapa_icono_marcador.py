# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_mapa', '0006_auto_20170816_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriamapa',
            name='icono_marcador',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
