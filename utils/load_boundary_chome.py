import os

from django.contrib.gis.utils import LayerMapping
from address.models import Chome


boundary_mapping = {
    'pref_code': 'PREF',
    'pref_name': 'PREF_NAME',
    'city_code': 'CITY',
    'city_name': 'CITY_NAME',
    'chome_code': 'KEY_CODE',
    'chome_name': 'S_NAME',
    'category': 'HCODE',
    'special_symbol_e': 'KIGO_E',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'area_max_f': 'AREA_MAX_F',
    'special_symbol_d': 'KIGO_D',
    'people_count': 'JINKO',
    'family_count': 'SETAI',
    'center_lng': 'X_CODE',
    'center_lat': 'Y_CODE',
    'mpoly': 'MULTIPOLYGON',
}


def run(path, verbose=True):
    if os.path.exists(path) and os.path.isdir(path):
        for name in os.listdir(path):
            if not name.endswith('.shp'):
                continue
            shp_file = os.path.join(path, name)
            lm = LayerMapping(Chome, shp_file, boundary_mapping, transform=False)
            lm.save(strict=True, verbose=verbose)
    else:
        print('指定されたフォルダーが存在しません。')
