# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20170731_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.TextField(),
        ),
    ]
