# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.TimeField(auto_now_add=True, null=True)),
                ('hora', models.DateField(auto_now_add=True, null=True)),
                ('titulo', models.CharField(default='MiRegión.co', max_length=100)),
                ('mensaje', models.CharField(max_length=140)),
            ],
        ),
    ]