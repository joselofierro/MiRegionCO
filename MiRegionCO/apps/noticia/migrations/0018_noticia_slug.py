# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0017_auto_20171103_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]