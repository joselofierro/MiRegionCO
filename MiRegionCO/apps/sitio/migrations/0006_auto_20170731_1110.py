# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_auto_20170729_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='id_facebook',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitio',
            name='id_instagram',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
