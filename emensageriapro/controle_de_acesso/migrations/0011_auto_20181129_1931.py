# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-29 19:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_de_acesso', '0010_auto_20181122_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True},
        ),
        migrations.AlterModelManagers(
            name='usuarios',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
