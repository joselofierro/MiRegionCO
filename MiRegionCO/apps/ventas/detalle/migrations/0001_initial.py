# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategoria_producto', '0001_initial'),
        ('producto', '0001_initial'),
        ('categoria_producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria_producto.CategoriaProducto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategoria_producto.Subcategoria')),
            ],
        ),
    ]
