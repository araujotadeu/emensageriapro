# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0007_auto_20181119_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivos',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='regrasdevalidacao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='relatorios',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventos',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventoshorarios',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosintervalos',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosocorrencias',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinfocorrencias',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocialocorrencias',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
    ]
