# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_auto_20170731_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitio',
            name='id_facebook',
        ),
        migrations.RemoveField(
            model_name='sitio',
            name='id_instagram',
        ),
        migrations.AlterField(
            model_name='sitio',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='instagram',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
