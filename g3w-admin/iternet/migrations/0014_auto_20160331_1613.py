# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iternet', '0013_auto_20160331_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementostradale',
            name='cod_gst',
            field=models.CharField(blank=True, choices=[('0', 'Stato'), ('09', 'Regione'), (b'', 'Provincia'), (b'B648', 'Comune'), ('999999', 'Privati/altro')], max_length=6, null=True),
        ),
    ]