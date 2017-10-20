# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import scrapy
import zipfile
import csv
import StringIO
import requests

from io import BytesIO


class PostcodeSpider(scrapy.Spider):
    name = 'post_code'

    start_urls = [
        'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip',
    ]

    post_url = 'http://127.0.0.1:8001/api/postcodes/'

    def parse(self, response):
        zip_file = zipfile.ZipFile(BytesIO(response.body))
        for name in zip_file.namelist():
            text = zip_file.read(name)
            reader = csv.reader(StringIO.StringIO(text))
            # header = next(reader)     # without header
            for row in reader:
                post_code = dict()
                post_code['city_code'] = row[0]
                post_code['post_code'] = row[2]
                post_code['pref_name'] = row[6].decode('shift-jis')
                post_code['city_name'] = row[7].decode('shift-jis')
                post_code['town_name'] = row[8].decode('shift-jis')
                post_code['pref_kana'] = row[3].decode('shift-jis')
                post_code['city_kana'] = row[4].decode('shift-jis')
                post_code['town_kana'] = row[5].decode('shift-jis')
                post_code['is_partial'] = row[9]
                post_code['is_multi_chome'] = row[11]
                post_code['is_multi_town'] = row[12]
                self.save_postcode(post_code)

    def save_postcode(self, data):
        r = requests.post(self.post_url, data=data)
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
