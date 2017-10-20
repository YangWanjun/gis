# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import zipfile
import StringIO
import csv
import requests
import re

from . import common
from .errors import FileNotExistsException


def sync_pref(url):
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
            save_data(url, {'code': code, 'name': name})


def sync_company(url):
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
            save_data(url, company)


def sync_line(url):
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
            line['lon'] = row[8]
            line['lat'] = row[9]
            line['zoom'] = row[10]
            line['status'] = row[11]
            line['sort'] = row[12]
            save_data(url, line)


def sync_station(url):
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
            line['pref'] = row[6]
            line['post_code'] = re.sub(r'[^0-9]+', '', row[7])
            line['address'] = row[8]
            line['lon'] = row[9]
            line['lat'] = row[10]
            line['open_date'] = row[11]
            line['close_date'] = row[12]
            line['status'] = row[13]
            line['sort'] = row[14]
            save_data(url, line)


def sync_station_connection(url):
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
            save_data(url, station_connection)


def save_data(post_url, data):
    r = requests.post(post_url, data=data)
    if  200 <= r.status_code < 300:
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
