# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('activacion_youtuber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='codigo',
            field=models.CharField(default=uuid.uuid4, max_length=25, primary_key=True, serialize=False),
        ),
    ]
