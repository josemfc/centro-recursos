# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0004_add_forums'),
    ]

    operations = [
        migrations.AddField(
            model_name='foro',
            name='titulo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]