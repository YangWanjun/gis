# -*- coding: UTF-8 -*-
# 市区町村単位のシェープファイルを県単位のシェープファイルに変換する。
#
#
import os


PATH = r'D:\workspace\gis\download\AzaAddress'
O_PATH = r'D:\workspace\gis\download\GIS_AZA'


shp_dict = dict()
for root, dirs, files in os.walk(PATH):
    for f in files:
        if f[-4:] == ".shp":
            city_code = os.path.basename(os.path.dirname(root))
            shp_path = os.path.join(root, f)
            pref_code = city_code[:2]
            if pref_code in shp_dict:
                shp_dict[pref_code].append(shp_path)
            else:
                shp_dict[pref_code] = [shp_path]

for pref_code, shp_list in shp_dict.items():
    print r'ogr2ogr -f "ESRI Shapefile" %s %s' % (
        os.path.join(O_PATH, 'GIS_AZA_%s' % pref_code),
        shp_list[0],
    )
    for shp_path in shp_list[1:]:
        print r'ogr2ogr -f "ESRI Shapefile" -append -update %s %s' % (
            os.path.join(O_PATH, 'GIS_AZA_%s' % pref_code),
            shp_list[0],
        )
