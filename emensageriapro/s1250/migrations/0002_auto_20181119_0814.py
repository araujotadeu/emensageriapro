# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0008_auto_20181118_2229'),
        ('s1250', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1250infoProcJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrprocjud', models.CharField(default=b'A', max_length=20)),
                ('codsusp', models.IntegerField(default=0)),
                ('vrcpnret', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vrratnret', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vrsenarnret', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocj_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocj_modificado_por', to='controle_de_acesso.Usuarios')),
            ],
            options={
                'ordering': ['s1250_tpaquis', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret'],
                'db_table': 's1250_infoprocj',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='s1250ideprodutor',
            options={'managed': True, 'ordering': ['s1250_tpaquis', 'tpinscprod', 'nrinscprod', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc', 'indopccp']},
        ),
        migrations.AlterModelOptions(
            name='s1250nfs',
            options={'managed': True, 'ordering': ['s1250_ideprodutor', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc']},
        ),
        migrations.AddField(
            model_name='s1250ideprodutor',
            name='indopccp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='nrinscprod',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='s1250_tpaquis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250ideprodutor_s1250_tpaquis', to='s1250.s1250tpAquis'),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='tpinscprod',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='codsusp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='nrprocjud',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='s1250_ideprodutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocjud_s1250_ideprodutor', to='s1250.s1250ideProdutor'),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrcpnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrratnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrsenarnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='dtemisnf',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='nrdocto',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='s1250_ideprodutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250nfs_s1250_ideprodutor', to='s1250.s1250ideProdutor'),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='indaquis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='s1250_evtaqprod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250tpaquis_s1250_evtaqprod', to='esocial.s1250evtAqProd'),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='vlrtotaquis',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AddField(
            model_name='s1250infoprocj',
            name='s1250_tpaquis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocj_s1250_tpaquis', to='s1250.s1250tpAquis'),
        ),
    ]
