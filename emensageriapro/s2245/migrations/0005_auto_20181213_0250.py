# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2245', '0004_auto_20181120_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2245infocomplem',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2245infocomplem',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2245infocomplem',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
