# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default='C', max_length=1),
        ),
    ]
