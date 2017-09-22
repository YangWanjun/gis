# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gis.settings')
django.setup()

from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal.field import OFTString
from django.contrib.gis.db.models import FloatField
from loader import models


aza_mapping = {
    'city_code': 'city_code',
    'jusho1': 'jusho1',
    'jusho2': 'jusho2',
    'jusho3': 'jusho3',
    'jcode1': 'jcode1',
    'jcode2': 'jcode2',
    'lon': 'lon',
    'lat': 'lat',
    'seido': 'seido',
    'geom': 'POINT',
}


root_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'download', 'AzaAddress')

def run_aza(verbose=True):
    LayerMapping.FIELD_TYPES.update({FloatField: OFTString})
    for p, dirs, files in os.walk(root_path):
        for f in files:
            if f[-4:] == ".shp":
                shp_path = os.path.join(p, f)
                lm = LayerMapping(models.AzaCode, shp_path, aza_mapping, transform=False, encoding='ISO8859-1')
                lm.save(strict=False, verbose=verbose)
                return


if __name__ == "__main__":
    run_aza()
