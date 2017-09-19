import scrapy
import os
import zipfile

from io import BytesIO
from urlparse import urljoin

from .. import common


class AddressSpider(scrapy.Spider):
    name = 'aza_address'

    start_urls = [
        'https://saigai.gsi.go.jp/jusho/download/index.html',
    ]

    def parse(self, response):
        for sel_link in response.xpath('//a[contains(@href, "pref")]'):
            name = sel_link.xpath('text()').extract_first()
            p_link = sel_link.xpath('@href').extract_first()
            a_link = urljoin(response.url, p_link)
            yield scrapy.Request(url=a_link, callback=self.parse_city, meta={'pref_name': name})

    def parse_city(self, response):
        pref_name = response.meta.get('pref_name')
        for sel_link in response.xpath('//li/a[contains(@href, "data")]'):
            name = sel_link.xpath('text()').extract_first()
            p_link = sel_link.xpath('@href').extract_first()
            a_link = urljoin(response.url, p_link)
            yield scrapy.Request(url=a_link, callback=self.save_address, meta={'pref_name': pref_name, 'city_name': name})

    def save_address(self, response):
        # pref_name = response.meta.get('pref_name')
        # city_name = response.meta.get('city_name')
        # file_name = '%s_%s' % (pref_name, city_name)
        path = os.path.join(common.get_storage_path(), 'AzaAddress')
        if not os.path.exists(path):
            os.mkdir(path)
        zip_ref = zipfile.ZipFile(BytesIO(response.body))
        zip_ref.extractall(path)
        zip_ref.close()
