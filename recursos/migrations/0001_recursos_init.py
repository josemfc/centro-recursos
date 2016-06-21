# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-15 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_pub', models.DateTimeField(verbose_name='fecha publicacion')),
                ('duracion', models.TimeField()),
                ('visualizaciones', models.IntegerField(default=0)),
                ('tipo', models.IntegerField(choices=[(0, 'video'), (1, 'pdf')], default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.Categoria')),
            ],
        ),
    ]
