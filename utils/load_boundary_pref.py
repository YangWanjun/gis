from django.contrib.gis.geos import MultiPolygon, Polygon
from django.db import connection

from addr.models import City, Pref
from utils import constants


def run():
    if City.objects.count() == 0:
        raise Exception('市区町村データがありません。')
    for i in range(1, 48):
        pref_code = '%02d' % i
        pref_name = constants.DICT_PREF[pref_code]
        qs = City.objects.filter(pref_code=pref_code)
        pref = Pref(pref_code=pref_code, pref_name=pref_name, people_count=0, family_count=0)
        mpoly = None
        for city in qs:
            pref.people_count += city.people_count or 0
            pref.family_count += city.family_count or 0
            if mpoly is None:
                mpoly = city.mpoly
            else:
                mpoly = mpoly.union(city.mpoly)
        if mpoly and isinstance(mpoly, Polygon):
            mpoly = MultiPolygon([mpoly])
        pref.mpoly = mpoly
        pref.save()
#
#
# def run2():
#     with connection.cursor() as cursor:
#         for i in range(1, 48):
#             pref_code = '%02d' % i
#             cursor.execute("""
#             insert into gis_pref (pref_code,pref_name,people_count,family_count,mpoly,created_date,updated_date,is_deleted)
#             select pref_code, max(pref_name), sum(people_count), sum(family_count), ST_Multi(ST_Union(mpoly)), now(), now(), false
#               from gis_city
#              where pref_code = %s
#              group by pref_code;""", [pref_code])
