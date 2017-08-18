# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import qdjango.models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0029_auto_20170523_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='tilestache_conf',
        ),
        migrations.AddField(
            model_name='layer',
            name='vectorjoins',
            field=models.TextField(blank=True, null=True, verbose_name='Layer relations'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to=qdjango.models.get_layer_data_file_path, verbose_name='Associated data file'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='layer_type',
            field=models.CharField(choices=[(b'postgres', 'Postgres'), (b'spatialite', 'SpatiaLite'), (b'raster', 'Raster'), (b'wfs', 'WFS'), (b'wms', 'WMS'), (b'ogr', 'OGR'), (b'gdal', 'GDAL'), (b'delimitedtext', 'CSV')], max_length=255, verbose_name='Type'),
        ),
    ]
