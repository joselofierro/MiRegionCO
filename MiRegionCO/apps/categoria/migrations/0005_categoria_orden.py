# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0004_auto_20170808_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='orden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]