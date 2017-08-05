# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imagen', '0001_initial'),
        ('categoria_mapa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('horario', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('telefono', models.CharField(max_length=30)),
                ('latitud', models.FloatField(max_length=30)),
                ('longitud', models.FloatField(max_length=30)),
                ('categoria', models.ManyToManyField(to='categoria_mapa.CategoriaMapa')),
                ('imagenes', models.ManyToManyField(to='imagen.Imagen')),
            ],
        ),
    ]
