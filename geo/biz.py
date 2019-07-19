from django.contrib.gis.geos import Point


def transform_point(lng, lat, srid_from, srid_to):
    """経度緯度の測地系変更

    :param lng: 経度
    :param lat: 緯度
    :param srid_from: 変換前の測地系
    :param srid_to: 変換後の測地系
    :return: 変換後の経度緯度
    """
    point = Point(float(lng), float(lat), srid=int(srid_from))
    point.transform(int(srid_to))
    return point.x, point.y
