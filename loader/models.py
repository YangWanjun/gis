# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.


class AzaCode(models.Model):
    ogc_fid = models.BigIntegerField(primary_key=True)
    city_code = models.CharField(max_length=80, verbose_name="市区町村コード")
    jusho1 = models.CharField(max_length=80)
    jusho2 = models.CharField(max_length=80)
    jusho3 = models.CharField(max_length=80)
    jcode1 = models.CharField(max_length=80)
    jcode2 = models.CharField(max_length=80)
    lon = models.FloatField()
    lat = models.FloatField()
    seido = models.CharField(max_length=80)

    wkb_geometry = models.PointField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'gis_aza'

    def __unicode__(self):
        return self.city_code
