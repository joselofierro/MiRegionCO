# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('noticia', '0015_noticia_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='mobile',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='web',
            field=models.BooleanField(default=True),
        ),
    ]