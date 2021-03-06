# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1060', '0002_auto_20180912_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1060alteracaofatorrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1060alteracaofatorrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1060alteracaofatorrisco',
            name='s1060_alteracao',
        ),
        migrations.RemoveField(
            model_name='s1060inclusaofatorrisco',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1060inclusaofatorrisco',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1060inclusaofatorrisco',
            name='s1060_inclusao',
        ),
        migrations.AlterModelOptions(
            name='s1060alteracao',
            options={'managed': True, 'ordering': ['s1060_evttabambiente', 'codamb', 'inivalid', 'fimvalid', 'dscamb', 'localamb', 'tpinsc', 'nrinsc', 'codlotacao']},
        ),
        migrations.AlterModelOptions(
            name='s1060inclusao',
            options={'managed': True, 'ordering': ['s1060_evttabambiente', 'codamb', 'inivalid', 'fimvalid', 'dscamb', 'localamb', 'tpinsc', 'nrinsc', 'codlotacao']},
        ),
        migrations.AddField(
            model_name='s1060alteracao',
            name='codlotacao',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='s1060inclusao',
            name='codlotacao',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1060alteracao',
            name='dscamb',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='s1060alteracao',
            name='localamb',
            field=models.IntegerField(choices=[(1, '1 - Estabelecimento do pr\xf3prio empregador'), (2, '2 - Estabelecimento de terceiros'), (3, '3 - Presta\xe7\xe3o de servi\xe7os em instala\xe7\xf5es de terceiros n\xe3o consideradas como lota\xe7\xf5es dos tipos 03 a 09 da Tabela 10')]),
        ),
        migrations.AlterField(
            model_name='s1060alteracao',
            name='nrinsc',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1060alteracao',
            name='tpinsc',
            field=models.IntegerField(blank=True, choices=[(1, '1 - CNPJ'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')], null=True),
        ),
        migrations.AlterField(
            model_name='s1060inclusao',
            name='dscamb',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='s1060inclusao',
            name='localamb',
            field=models.IntegerField(choices=[(1, '1 - Estabelecimento do pr\xf3prio empregador'), (2, '2 - Estabelecimento de terceiros'), (3, '3 - Presta\xe7\xe3o de servi\xe7os em instala\xe7\xf5es de terceiros n\xe3o consideradas como lota\xe7\xf5es dos tipos 03 a 09 da Tabela 10')]),
        ),
        migrations.AlterField(
            model_name='s1060inclusao',
            name='nrinsc',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1060inclusao',
            name='tpinsc',
            field=models.IntegerField(blank=True, choices=[(1, '1 - CNPJ'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')], null=True),
        ),
        migrations.DeleteModel(
            name='s1060alteracaofatorRisco',
        ),
        migrations.DeleteModel(
            name='s1060inclusaofatorRisco',
        ),
    ]
