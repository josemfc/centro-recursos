# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 11:19
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_descripcion_textField'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.Foro')),
            ],
        ),
    ]
