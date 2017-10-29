# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.core.validators import RegexValidator

from addr.models import Pref
from utils.django_base import BaseModel
from utils import constants


# Create your models here.
class Company(BaseModel):
    code = models.IntegerField(primary_key=True, verbose_name="事業者コード")
    rr_code = models.CharField(max_length=2, verbose_name="鉄道コード", validators=(RegexValidator(r"^\d{2}$"),))
    name = models.CharField(max_length=80, verbose_name="事業者名(一般)")
    kana = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者名(一般・カナ)")
    name_full = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者名(正式名称)")
    name_alias = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者名(略称)")
    site = models.URLField(blank=True, null=True, verbose_name="Webサイト")
    segment = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_BUSINESS_SEGMENT, verbose_name="事業者区分"
    )
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )
    sort = models.IntegerField(blank=True, null=True, verbose_name="並び順")

    class Meta:
        db_table = 'gis_company'
        ordering = ['sort']
        verbose_name = "事業者"
        verbose_name_plural = "事業者一覧"

    def __unicode__(self):
        return self.name


class Line(BaseModel):
    code = models.IntegerField(primary_key=True, verbose_name="路線コード")
    company = models.ForeignKey(Company, verbose_name="事業者")
    name = models.CharField(max_length=80, verbose_name="路線名称(一般)")
    kana = models.CharField(max_length=80, blank=True, null=True, verbose_name="路線名称(一般・カナ)")
    name_full = models.CharField(max_length=80, blank=True, null=True, verbose_name="路線名称(正式名称)")
    segment = models.CharField(max_length=1, blank=True, null=True, verbose_name="路線区分")
    # lon = models.FloatField(blank=True, null=True, verbose_name="経度", help_text="路線表示時の中央経度")
    # lat = models.FloatField(blank=True, null=True, verbose_name="緯度", help_text="路線表示時の中央緯度")
    point = models.PointField(blank=True, null=True, verbose_name="座標")
    zoom = models.IntegerField(
        blank=True, null=True, verbose_name="路線表示時のGoogleMap倍率",
        help_text="600x600でおおよそすべてが収まる程度"
    )
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )
    sort = models.IntegerField(blank=True, null=True, verbose_name="並び順")

    class Meta:
        db_table = 'gis_line'
        ordering = ['sort']
        verbose_name = "路線"
        verbose_name_plural = "路線一覧"

    def __unicode__(self):
        return self.name


class Station(BaseModel):
    code = models.IntegerField(primary_key=True, verbose_name="駅コード")
    line = models.ForeignKey(Line, verbose_name="路線")
    name = models.CharField(max_length=80, verbose_name="駅名称")
    pref = models.ForeignKey(Pref, blank=True, null=True, verbose_name="都道府県")
    post_code = models.CharField(max_length=7, blank=True, null=True, verbose_name="駅郵便番号")
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="住所")
    # lon = models.FloatField(blank=True, null=True, verbose_name="経度", help_text="世界測地系")
    # lat = models.FloatField(blank=True, null=True, verbose_name="緯度", help_text="世界測地系")
    point = models.PointField(blank=True, null=True, verbose_name="座標")
    open_date = models.DateField(blank=True, null=True, verbose_name="開業年月日")
    close_date = models.DateField(blank=True, null=True, verbose_name="廃止年月日")
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )
    sort = models.IntegerField(blank=True, null=True, verbose_name="並び順")

    class Meta:
        db_table = 'gis_station'
        ordering = ['sort']
        verbose_name = "駅"
        verbose_name_plural = "駅一覧"

    def __unicode__(self):
        return self.name


class StationConnection(BaseModel):
    line = models.ForeignKey(Line, verbose_name="路線")
    station1 = models.ForeignKey(Station, related_name="start_station_set", verbose_name="駅１")
    station2 = models.ForeignKey(Station, related_name="end_station_set", verbose_name="駅２")

    class Meta:
        db_table = 'gis_station_connection'
        verbose_name = "接続駅"
        verbose_name_plural = "接続駅一覧"

    def __unicode__(self):
        return "%s～%s" % (unicode(self.station1), unicode(self.station2))
