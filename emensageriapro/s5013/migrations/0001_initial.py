# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controle_de_acesso', '0008_auto_20181118_2229'),
        ('esocial', '0005_auto_20181119_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='s5013basePerAntE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpvalore', models.IntegerField(choices=[(13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], default=0)),
                ('basefgtse', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperante_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperante_modificado_por', to='controle_de_acesso.Usuarios')),
            ],
            options={
                'ordering': ['s5013_infobaseperante', 'tpvalore', 'basefgtse'],
                'db_table': 's5013_baseperante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5013basePerApur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpvalor', models.IntegerField(choices=[(11, '11 - Base de C\xe1lculo do FGTS'), (12, '12 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio'), (13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (15, '15 - Base de C\xe1lculo do FGTS - Aprendiz'), (16, '16 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (21, '21 - Base de C\xe1lculo do FGTS Rescis\xf3rio'), (22, '22 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (23, '23 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (27, '27 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aprendiz'), (28, '28 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (29, '29 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], default=0)),
                ('basefgts', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperapur_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperapur_modificado_por', to='controle_de_acesso.Usuarios')),
                ('s5013_evtfgts', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperapur_s5013_evtfgts', to='esocial.s5013evtFGTS')),
            ],
            options={
                'ordering': ['s5013_evtfgts', 'tpvalor', 'basefgts'],
                'db_table': 's5013_baseperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5013dpsPerAntE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpdpse', models.IntegerField(choices=[(53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz')], default=0)),
                ('vrfgtse', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperante_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperante_modificado_por', to='controle_de_acesso.Usuarios')),
            ],
            options={
                'ordering': ['s5013_infodpsperante', 'tpdpse', 'vrfgtse'],
                'db_table': 's5013_dpsperante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5013dpsPerApur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpdps', models.IntegerField(choices=[(51, '51 - Dep\xf3sito do FGTS'), (52, '52 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio'), (53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (55, '55 - Dep\xf3sito do FGTS - Aprendiz'), (56, '56 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (61, '61 - Dep\xf3sito do FGTS Rescis\xf3rio'), (62, '62 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (63, '63 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (67, '67 - Dep\xf3sito do FGTS Rescis\xf3rio - Aprendiz'), (68, '68 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (69, '69 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz')], default=0)),
                ('vrfgts', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperapur_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperapur_modificado_por', to='controle_de_acesso.Usuarios')),
                ('s5013_evtfgts', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperapur_s5013_evtfgts', to='esocial.s5013evtFGTS')),
            ],
            options={
                'ordering': ['s5013_evtfgts', 'tpdps', 'vrfgts'],
                'db_table': 's5013_dpsperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5013infoBasePerAntE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perref', models.CharField(default=b'A', max_length=7)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infobaseperante_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infobaseperante_modificado_por', to='controle_de_acesso.Usuarios')),
                ('s5013_evtfgts', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infobaseperante_s5013_evtfgts', to='esocial.s5013evtFGTS')),
            ],
            options={
                'ordering': ['s5013_evtfgts', 'perref'],
                'db_table': 's5013_infobaseperante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5013infoDpsPerAntE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perref', models.CharField(default=b'A', max_length=7)),
                ('criado_em', models.DateTimeField()),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infodpsperante_criado_por', to='controle_de_acesso.Usuarios')),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infodpsperante_modificado_por', to='controle_de_acesso.Usuarios')),
                ('s5013_evtfgts', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infodpsperante_s5013_evtfgts', to='esocial.s5013evtFGTS')),
            ],
            options={
                'ordering': ['s5013_evtfgts', 'perref'],
                'db_table': 's5013_infodpsperante',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s5013dpsperante',
            name='s5013_infodpsperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperante_s5013_infodpsperante', to='s5013.s5013infoDpsPerAntE'),
        ),
        migrations.AddField(
            model_name='s5013baseperante',
            name='s5013_infobaseperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperante_s5013_infobaseperante', to='s5013.s5013infoBasePerAntE'),
        ),
    ]
