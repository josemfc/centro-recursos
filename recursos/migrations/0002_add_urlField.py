# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-15 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_recursos_init'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='enlace',
            field=models.URLField(default='http://google.es'),
            preserve_default=False,
        ),
    ]