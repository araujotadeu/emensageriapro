# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1202', '0002_auto_20180912_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - IRRF'), (2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')]),
        ),
    ]
