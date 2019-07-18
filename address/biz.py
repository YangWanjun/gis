import re

from django.db import connection


def transform_point(lng, lat, srid_from, srid_to):
    lng = float(lng)
    lat = float(lat)
    srid_from = int(srid_from)
    srid_to = int(srid_to)
    with connection.cursor() as cursor:
        cursor.execute("SELECT ST_AsText(ST_Transform(ST_GeomFromText('POINT(%s %s)', %s), %s))", [
            lng, lat, srid_from, srid_to
        ])
        row = cursor.fetchone()
    lng = lat = None
    if len(row) > 0:
        m = re.findall(r'(\d+\.\d+)\s+(\d+\.\d+)', row[0])
        if m:
            lng, lat = m[0]
            lng = float(lng)
            lat = float(lat)
    return lng, lat
