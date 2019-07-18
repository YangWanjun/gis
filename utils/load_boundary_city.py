import os

from django.contrib.gis.utils import LayerMapping
from address.models import City


boundary_mapping = {
    # 'pref_code': 'JCODE',
    'pref_name': 'KEN',
    'city_code': 'JCODE',
    'city_name': 'SIKUCHOSON',
    'city_name_en': 'CITY_ENG',
    'gun_name': 'GUN',
    'people_count': 'P_NUM',
    'family_count': 'H_NUM',
    'mpoly': 'MULTIPOLYGON',
}


def run(path, verbose=True):
    if os.path.exists(path) and os.path.isdir(path):
        for name in os.listdir(path):
            if not name.endswith('.shp'):
                continue
            shp_file = os.path.join(path, name)
            lm = LayerMapping(City, shp_file, boundary_mapping, transform=True)
            lm.save(strict=True, verbose=verbose)
    else:
        print('指定されたフォルダーが存在しません。')
