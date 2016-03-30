# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 08:24
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessi',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('cod_acc', models.CharField(blank=True, max_length=27, null=True)),
                ('tip_acc', models.CharField(blank=True, max_length=8, null=True)),
                ('cod_ele', models.CharField(blank=True, max_length=15, null=True)),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('pas_car', models.CharField(blank=True, max_length=1, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=3003)),
            ],
            options={
                'db_table': 'accessi',
            },
        ),
        migrations.CreateModel(
            name='Archi',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('cod_ele', models.CharField(blank=True, max_length=15, null=True)),
                ('nod_ini', models.CharField(blank=True, max_length=15, null=True)),
                ('nod_fin', models.CharField(blank=True, max_length=15, null=True)),
                ('cod_sta', models.CharField(blank=True, max_length=6, null=True)),
                ('cod_sed', models.CharField(blank=True, max_length=6, null=True)),
                ('tip_ele', models.CharField(blank=True, max_length=6, null=True)),
                ('cls_tcn', models.CharField(blank=True, max_length=6, null=True)),
                ('tip_gst', models.CharField(blank=True, max_length=6, null=True)),
                ('cod_gst', models.CharField(blank=True, max_length=6, null=True)),
                ('sot_pas', models.CharField(blank=True, max_length=6, null=True)),
                ('lng', models.IntegerField(blank=True, null=True)),
                ('cmp_ele', models.CharField(blank=True, max_length=9, null=True)),
                ('cod_reg', models.CharField(blank=True, max_length=29, null=True)),
                ('org', models.CharField(blank=True, max_length=6, null=True)),
                ('cls_lrg', models.CharField(blank=True, max_length=6, null=True)),
                ('cod_top', models.CharField(blank=True, max_length=29, null=True)),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('x_from', models.FloatField(blank=True, null=True)),
                ('y_from', models.FloatField(blank=True, null=True)),
                ('x_to', models.FloatField(blank=True, null=True)),
                ('y_to', models.FloatField(blank=True, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=3003)),
            ],
            options={
                'db_table': 'archi',
            },
        ),
        migrations.CreateModel(
            name='Civici',
            fields=[
                ('cod_civ', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('cod_acc_in', models.CharField(blank=True, max_length=19, null=True)),
                ('num_civ', models.FloatField(blank=True, null=True)),
                ('esp_civ', models.CharField(blank=True, max_length=9, null=True)),
                ('cod_com', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_top', models.CharField(blank=True, max_length=18, null=True)),
                ('cod_acc_es', models.CharField(blank=True, max_length=19, null=True)),
            ],
            options={
                'db_table': 'civici',
            },
        ),
        migrations.CreateModel(
            name='CiviciInfo',
            fields=[
                ('cod_civ', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('tip_opz', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'civici_info',
            },
        ),
        migrations.CreateModel(
            name='ContrNc16223',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('toponimo', models.CharField(blank=True, max_length=254, null=True)),
                ('civico', models.CharField(blank=True, max_length=255, null=True)),
                ('esponente', models.CharField(blank=True, max_length=2, null=True)),
                ('int_uff', models.CharField(blank=True, max_length=254, null=True)),
                ('tipoimm', models.CharField(blank=True, max_length=254, null=True)),
                ('operazioni', models.SmallIntegerField(blank=True, null=True)),
                ('dt_agg', models.DateField(blank=True, null=True)),
                ('dt_ins', models.DateField(blank=True, null=True)),
                ('variaz', models.CharField(blank=True, max_length=60, null=True)),
                ('cod_strade', models.BigIntegerField(blank=True, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=3003)),
            ],
            options={
                'db_table': 'contr_nc_16223',
            },
        ),
        migrations.CreateModel(
            name='Interni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_civ', models.CharField(blank=True, max_length=19, null=True)),
                ('interno', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'interni',
            },
        ),
        migrations.CreateModel(
            name='LegClsLrg',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cls_lrg',
            },
        ),
        migrations.CreateModel(
            name='LegClsTcn',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cls_tcn',
            },
        ),
        migrations.CreateModel(
            name='LegCmpEle',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cmp_ele',
            },
        ),
        migrations.CreateModel(
            name='LegCodDug',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cod_dug',
            },
        ),
        migrations.CreateModel(
            name='LegCodSed',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cod_sed',
            },
        ),
        migrations.CreateModel(
            name='LegCodSta',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cod_sta',
            },
        ),
        migrations.CreateModel(
            name='LegOrg',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_org',
            },
        ),
        migrations.CreateModel(
            name='LegSotPas',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_sot_pas',
            },
        ),
        migrations.CreateModel(
            name='LegTipAcc',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_tip_acc',
            },
        ),
        migrations.CreateModel(
            name='LegTipEle',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_tip_ele',
            },
        ),
        migrations.CreateModel(
            name='LegTipGnz',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_tip_gnz',
            },
        ),
        migrations.CreateModel(
            name='LegTipGst',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_tip_gst',
            },
        ),
        migrations.CreateModel(
            name='Nodi',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('cod_gnz', models.CharField(blank=True, max_length=15, null=True)),
                ('tip_gnz', models.CharField(blank=True, max_length=6, null=True)),
                ('org', models.CharField(blank=True, max_length=6, null=True)),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=3003)),
            ],
            options={
                'db_table': 'nodi',
            },
        ),
        migrations.CreateModel(
            name='Toponimo',
            fields=[
                ('cod_top', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('den_uff', models.CharField(blank=True, max_length=41, null=True)),
                ('cod_com', models.CharField(blank=True, max_length=10, null=True)),
                ('cod_via', models.CharField(blank=True, max_length=11, null=True)),
                ('den_senza', models.CharField(blank=True, max_length=49, null=True)),
                ('cod_dug', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'toponimo',
            },
        ),
    ]
