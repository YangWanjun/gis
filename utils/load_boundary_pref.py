from django.contrib.gis.geos import GEOSGeometry
from addr.models import City
from utils import constants


def main():
    if City.objects.count() > 0:
        raise Exception('市区町村データがありません。')
    for i in range(1, 48):
        pref_code = '%02d' % i
        pref_name = constants.DICT_PREF[pref_code]
        qs = City.objects.filter(pref_code=pref_code)
        for city in qs:
            pass


if __name__ == '__main__':
    main()
