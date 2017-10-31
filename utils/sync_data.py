# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import zipfile
import StringIO
import csv
import requests
import re
import urlparse

import common
from errors import FileNotExistsException, SettingException


HOST_NAME = 'http://127.0.0.1:8001'


def sync_pref():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    url_add_pref = urlparse.urljoin(HOST_NAME, '/api/pref_list/')
    path = os.path.join(common.get_data_path(), 'pref.zip')
    if not os.path.exists(path):
        raise FileNotExistsException(path)
    zip_file = zipfile.ZipFile(path, 'r')
    for file_name in zip_file.namelist():
        text = zip_file.read(file_name)
        reader = csv.reader(StringIO.StringIO(text))
        header = next(reader)  # without header
        for row in reader:
            code, name = row[0], row[1]
            print code, name
            code = '%02d' % int(code)
            save_data(url_add_pref, {'code': code, 'name': name})


def sync_company():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    url_add_company = urlparse.urljoin(HOST_NAME, '/api/company_list/')
    path = os.path.join(common.get_data_path(), 'company.zip')
    if not os.path.exists(path):
        raise FileNotExistsException(path)
    zip_file = zipfile.ZipFile(path, 'r')
    for file_name in zip_file.namelist():
        text = zip_file.read(file_name)
        reader = csv.reader(StringIO.StringIO(text))
        header = next(reader)  # without header
        for row in reader:
            company = dict()
            company['code'] = row[0]
            company['rr_code'] = row[1]
            company['name'] = row[2]
            company['kana'] = row[3]
            company['name_full'] = row[4]
            company['name_alias'] = row[5]
            company['site'] = row[6]
            company['segment'] = row[7]
            company['status'] = row[8]
            company['sort'] = row[9]
            save_data(url_add_company, company)


def sync_line():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    url_add_line = urlparse.urljoin(HOST_NAME, '/api/line_list/')
    path = os.path.join(common.get_data_path(), 'line.zip')
    if not os.path.exists(path):
        raise FileNotExistsException(path)
    zip_file = zipfile.ZipFile(path, 'r')
    for file_name in zip_file.namelist():
        text = zip_file.read(file_name)
        reader = csv.reader(StringIO.StringIO(text))
        header = next(reader)  # without header
        for row in reader:
            line = dict()
            line['code'] = row[0]
            line['company'] = row[1]
            line['name'] = row[2]
            line['kana'] = row[3]
            line['name_full'] = row[6]
            line['segment'] = row[7]
            # line['lon'] = row[8]
            # line['lat'] = row[9]
            line['point'] = 'POINT (%s %s)' % (row[8], row[9])
            line['zoom'] = row[10]
            line['status'] = row[11]
            line['sort'] = row[12]
            save_data(url_add_line, line)


def sync_station():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    url_add_station = urlparse.urljoin(HOST_NAME, '/api/station_list/')
    path = os.path.join(common.get_data_path(), 'station.zip')
    if not os.path.exists(path):
        raise FileNotExistsException(path)
    zip_file = zipfile.ZipFile(path, 'r')
    for file_name in zip_file.namelist():
        text = zip_file.read(file_name)
        reader = csv.reader(StringIO.StringIO(text))
        header = next(reader)  # without header
        for row in reader:
            line = dict()
            line['code'] = row[0]
            line['name'] = row[2]
            line['line'] = row[5]
            line['pref'] = '%02d' % int(row[6])
            line['post_code'] = re.sub(r'[^0-9]+', '', row[7])
            line['address'] = row[8]
            # line['lon'] = row[9]
            # line['lat'] = row[10]
            line['point'] = 'POINT (%s %s)' % (row[9], row[10])
            line['open_date'] = row[11]
            line['close_date'] = row[12]
            line['status'] = row[13]
            line['sort'] = row[14]
            save_data(url_add_station, line)


def sync_station_connection():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    url_add_join = urlparse.urljoin(HOST_NAME, '/api/station_connection_list/')
    path = os.path.join(common.get_data_path(), 'join.zip')
    if not os.path.exists(path):
        raise FileNotExistsException(path)
    zip_file = zipfile.ZipFile(path, 'r')
    for file_name in zip_file.namelist():
        text = zip_file.read(file_name)
        reader = csv.reader(StringIO.StringIO(text))
        header = next(reader)  # without header
        for row in reader:
            station_connection = dict()
            station_connection['line'] = row[0]
            station_connection['station1'] = row[1]
            station_connection['station2'] = row[2]
            save_data(url_add_join, station_connection)


def sync_city():
    if not HOST_NAME:
        raise SettingException('HOST_NAME')
    path = os.path.join(common.get_data_path(), 'city_code')
    if not os.path.exists(path):
        raise FileNotExistsException(path)

    url_add_city = urlparse.urljoin(HOST_NAME, '/api/city_list/')
    url_add_aza = urlparse.urljoin(HOST_NAME, '/api/aza_list/')
    for zip_name in os.listdir(path):
        if os.path.splitext(zip_name)[-1] != '.zip':
            continue
        zip_path = os.path.join(path, zip_name)
        zip_file = zipfile.ZipFile(zip_path, 'r')
        for file_name in zip_file.namelist():
            if os.path.splitext(file_name)[-1] != '.csv':
                continue
            text = zip_file.read(file_name)
            reader = csv.reader(StringIO.StringIO(text))
            header = next(reader)  # without header
            prev_city_code = ''
            for row in reader:
                if prev_city_code != row[2]:
                    city = dict()
                    city['pref'] = row[0]
                    city['code'] = row[2]
                    try:
                        city['name'] = row[3].decode('cp932')
                    except:
                        print city['code'], "市区町村名文字コードエラー"
                        city['name'] = row[3]
                    save_data(url_add_city, city)
                    prev_city_code = row[2]
                aza = dict()
                aza['pref'] = row[0]
                aza['city'] = row[2]
                aza['code'] = row[4]
                try:
                    aza['name'] = row[5].decode('cp932')
                except:
                    print aza['code'], "町丁字文字コードエラー"
                    aza['name'] = row[5]
                aza['point'] = 'POINT (%s %s)' % (row[7], row[6])
                save_data(url_add_aza, aza)


def save_data(post_url, data):
    r = requests.post(post_url, data=data)
    if 200 <= r.status_code < 300:
        # 2xx Success 成功
        pass
    elif 300 <= r.status_code < 400:
        # 3xx Redirection リダイレクション
        pass
    elif 400 <= r.status_code < 500:
        # 4xx Client Error クライアントエラー
        print r.content
    elif 500 <= r.status_code:
        # 5xx Server Error サーバエラー
        print r.content


if __name__ == '__main__':
    sync_city()