# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 04:29
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AzaCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(max_length=80, verbose_name='\u5e02\u533a\u753a\u6751\u30b3\u30fc\u30c9')),
                ('jusho1', models.CharField(max_length=80)),
                ('jusho2', models.CharField(max_length=80)),
                ('jusho3', models.CharField(max_length=80)),
                ('jcode1', models.CharField(max_length=80)),
                ('jcode2', models.CharField(max_length=80)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('seido', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'db_table': 'gis_aza',
            },
        ),
    ]
