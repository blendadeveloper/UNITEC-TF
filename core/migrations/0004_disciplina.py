# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171112_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.CharField(max_length=200)),
                ('conteudo', models.CharField(max_length=200)),
            ],
        ),
    ]
