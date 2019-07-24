import os

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos.polygon import Polygon
from django.contrib.gis.geos.collections import MultiPolygon
from addr.models import City


# boundary_mapping = {
#     # 'pref_code': 'JCODE',
#     'pref_name': 'KEN',
#     'city_code': 'JCODE',
#     'city_name': 'SIKUCHOSON',
#     'city_name_en': 'CITY_ENG',
#     'gun_name': 'GUN',
#     'people_count': 'P_NUM',
#     'family_count': 'H_NUM',
#     'mpoly': 'MULTIPOLYGON',
# }


def run(path, verbose=True):
    if os.path.exists(path) and os.path.isdir(path):
        for name in os.listdir(path):
            if not name.endswith('.shp'):
                continue
            shp_file = os.path.join(path, name)
            # lm = LayerMapping(City, shp_file, boundary_mapping, transform=True)
            # lm.save(strict=True, verbose=verbose)
            ds = DataSource(shp_file)
            layer = ds[0]
            for feature in layer:
                mpoly = MultiPolygon.from_ewkt(feature.geom.ewkt)
                if isinstance(mpoly, Polygon):
                    mpoly = MultiPolygon([mpoly])
                City.objects.create(
                    pref_code=feature.get('JCODE')[:2],
                    pref_name=feature.get('KEN'),
                    city_code=feature.get('JCODE'),
                    city_name=feature.get('SIKUCHOSON'),
                    city_name_en=feature.get('CITY_ENG'),
                    gun_name=feature.get('GUN'),
                    people_count=feature.get('P_NUM'),
                    family_count=feature.get('H_NUM'),
                    mpoly=mpoly,
                )
    else:
        print('指定されたフォルダーが存在しません。')
