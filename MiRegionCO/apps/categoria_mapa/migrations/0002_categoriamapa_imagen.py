# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_mapa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriamapa',
            name='imagen',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
