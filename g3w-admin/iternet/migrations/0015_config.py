# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0013_layer_tilestache_conf'),
        ('iternet', '0014_auto_20160331_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qdjango_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qdjango.Project')),
            ],
        ),
    ]