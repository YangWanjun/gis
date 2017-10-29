# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.core.validators import RegexValidator

from utils.django_base import BaseModel


# Create your models here.
class Pref(BaseModel):
    code = models.CharField(max_length=2, primary_key=True, verbose_name="都道府県コード")
    name = models.CharField(max_length=20, unique=True, verbose_name="都道府県名称")

    class Meta:
        db_table = 'gis_pref'
        ordering = ['code']
        verbose_name = "都道府県"
        verbose_name_plural = "都道府県一覧"

    def __unicode__(self):
        return self.name


class City(BaseModel):
    code = models.CharField(max_length=5, primary_key=True, verbose_name="市区町村コード")
    name = models.CharField(max_length=30, verbose_name="市区町村名称")
    pref = models.ForeignKey(Pref, verbose_name="都道府県")

    class Meta:
        db_table = 'gis_city'
        ordering = ['code']
        verbose_name = "市区町村"
        verbose_name_plural = "市区町村一覧"

    def __unicode__(self):
        return self.name


class Aza(BaseModel):
    code = models.CharField(max_length=12, primary_key=True, verbose_name="大字町丁目コード")
    name = models.CharField(max_length=30, verbose_name="大字町丁目名称")
    city = models.ForeignKey(City, verbose_name="市区町村")
    pref = models.ForeignKey(Pref, verbose_name="都道府県")
    point = models.PointField(blank=True, null=True, verbose_name="座標")

    class Meta:
        db_table = 'gis_aza'
        ordering = ['code']
        verbose_name = "大字町丁目"
        verbose_name_plural = "大字町丁目一覧"

    def __unicode__(self):
        return self.name


class Postcode(BaseModel):
    city_code = models.CharField(
        max_length=5, validators=(RegexValidator(regex=r"^\d{5}$"),), verbose_name=u"市区町村コード"
    )
    post_code = models.CharField(
        max_length=7, unique=True, validators=(RegexValidator(regex=r"^\d{7}$"),), verbose_name=u"郵便番号"
    )
    pref_name = models.CharField(max_length=15, verbose_name="都道府県名称")
    city_name = models.CharField(max_length=15, verbose_name="市区町村名称")
    town_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="町域名称")
    pref_kana = models.CharField(max_length=15, verbose_name="度道府県カナ")
    city_kana = models.CharField(max_length=15, verbose_name="市区町村カナ")
    town_kana = models.CharField(max_length=50, blank=True, null=True, verbose_name="町域カナ")
    is_partial = models.BooleanField(
        default=False, verbose_name="町域の一部",
        help_text="一町域が二以上の郵便番号で表される場合の表示（「1」は該当、「0」は該当せず）"
    )
    is_multi_chome = models.BooleanField(
        default=False, verbose_name="複数の丁目",
        help_text="丁目を有する町域の場合の表示（「1」は該当、「0」は該当せず）"
    )
    is_multi_town = models.BooleanField(
        default=False, verbose_name="複数町域あり",
        help_text="一つの郵便番号で二以上の町域を表す場合の表示（「1」は該当、「0」は該当せず）"
    )

    class Meta:
        db_table = 'gis_post_code'
        verbose_name = "郵便番号"
        verbose_name_plural = '郵便番号一覧'

    def __unicode__(self):
        return self.post_code
