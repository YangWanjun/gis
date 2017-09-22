# -*- coding: UTF-8 -*-
# 市区町村単位のシェープファイルを県単位のシェープファイルに変換する。
#
#
import os


PATH = r'D:\workspace\gis\download\AzaAddress'
O_PATH = r'D:\workspace\gis\download\GIS_AZA'


print "SET SHAPE_ENCODING=CP932"
shp_dict = dict()
for root, dirs, files in os.walk(PATH):
    for f in files:
        if f[-4:] == ".shp":
            shp_path = os.path.join(root, f)
            print r'ogr2ogr -append -update -f "PostgreSQL" "PG:host=localhost user=postgres dbname=gis_addr password=root" %s -nln gis_aza' % shp_path
            break
