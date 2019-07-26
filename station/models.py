from django.contrib.gis.db import models

from utils import constants
from utils.base_models import BaseModel


# Create your models here.
class Company(BaseModel):
    company_code = models.IntegerField(primary_key=True, verbose_name="事業者コード")
    railway_code = models.IntegerField(verbose_name="鉄道コード")
    company_name = models.CharField(max_length=80, verbose_name="事業者名")
    company_kana = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者カナ")
    company_full_name = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者名(正式名称)")
    company_short_name = models.CharField(max_length=80, blank=True, null=True, verbose_name="事業者名(略称)")
    company_url = models.URLField(blank=True, null=True, verbose_name="Webサイト")
    company_type = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_COMPANY_TYPE, verbose_name="事業者区分"
    )
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )

    class Meta:
        db_table = 'gis_railway_company'
        default_permissions = ()
        ordering = ('company_code',)
        verbose_name = "事業者"
        verbose_name_plural = "事業者一覧"

    def __str__(self):
        return self.company_name


class Route(BaseModel):
    line_code = models.IntegerField(
        primary_key=True, verbose_name="路線コード",
        help_text="整数5桁　鉄道コード + エリアコード + 連番　※新幹線は4桁"
    )
    company = models.ForeignKey(Company, db_column='company_code', on_delete=models.PROTECT, verbose_name="事業者コード")
    line_name = models.CharField(max_length=80, verbose_name="路線名称")
    line_kana = models.CharField(max_length=80, verbose_name="路線カナ")
    line_full_name = models.CharField(max_length=80, blank=True, null=True, verbose_name="路線名称(正式名称)")
    color_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="路線カラーコード")
    color_name = models.CharField(max_length=10, blank=True, null=True, verbose_name="路線カラー名称")
    line_type = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_LINE_TYPE, verbose_name="路線区分"
    )
    center_lng = models.FloatField(blank=True, null=True, verbose_name="路線表示時の中央経度")
    center_lat = models.FloatField(blank=True, null=True, verbose_name="路線表示時の中央緯度")
    zoom = models.IntegerField(blank=True, null=True, verbose_name="路線表示時のGoogleMap倍率")
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )

    class Meta:
        db_table = 'gis_railway_route'
        default_permissions = ()
        ordering = ('line_code',)
        verbose_name = "路線"
        verbose_name_plural = "路線一覧"

    def __str__(self):
        return self.line_name


class Station(BaseModel):
    station_code = models.IntegerField(primary_key=True, verbose_name="駅コード", help_text="整数7桁 ※新幹線は6桁")
    station_group_code = models.IntegerField(verbose_name="駅グループコード")
    station_name = models.CharField(max_length=80, verbose_name="駅名称")
    station_kana = models.CharField(max_length=80, blank=True, null=True, verbose_name="駅カナ")
    station_name_en = models.CharField(max_length=80, blank=True, null=True, verbose_name="駅カナ")
    route = models.ForeignKey(Route, db_column='line_code', on_delete=models.PROTECT, verbose_name="路線")
    pref_code = models.CharField(max_length=2, verbose_name="都道府県コード")
    post_code = models.CharField(max_length=8, blank=True, null=True, verbose_name="駅郵便番号")
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="住所")
    lng = models.FloatField(blank=True, null=True, verbose_name="経度")
    lat = models.FloatField(blank=True, null=True, verbose_name="緯度")
    point = models.PointField(blank=True, null=True, verbose_name="座標")
    open_date = models.DateField(blank=True, null=True, verbose_name="開業年月日")
    close_date = models.DateField(blank=True, null=True, verbose_name="廃止年月日")
    status = models.CharField(
        max_length=1, blank=True, null=True, choices=constants.CHOICE_STATION_STATUS, verbose_name="状態"
    )

    class Meta:
        db_table = 'gis_station'
        default_permissions = ()
        ordering = ('station_code',)
        verbose_name = "駅"
        verbose_name_plural = "駅一覧"

    def __str__(self):
        return self.station_name


class JoinStation(BaseModel):
    route = models.ForeignKey(Route, db_column='line_code', on_delete=models.PROTECT, verbose_name="路線コード")
    station1 = models.ForeignKey(
        Station, db_column='station_code1', on_delete=models.PROTECT, related_name='join_station1_set',
        verbose_name="駅コード１"
    )
    station2 = models.ForeignKey(
        Station, db_column='station_code2', on_delete=models.PROTECT, related_name='join_station2_set',
        verbose_name="駅コード２"
    )

    class Meta:
        db_table = 'gis_join_station'
        default_permissions = ()
        ordering = ('route', 'station1', 'station2')
        verbose_name = "接続駅"
        verbose_name_plural = "接続駅一覧"

