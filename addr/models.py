from django.contrib.gis.db import models
from django.core.validators import RegexValidator, validate_comma_separated_integer_list

from utils import constants
from utils.base_models import BaseModel


# Create your models here.
class Pref(BaseModel):
    pref_code = models.CharField(max_length=2, primary_key=True, verbose_name="都道府県番号")
    pref_name = models.CharField(max_length=20, verbose_name="都道府県名称")
    people_count = models.IntegerField(blank=True, null=True, verbose_name="人口")
    family_count = models.IntegerField(blank=True, null=True, verbose_name="世帯数")
    mpoly = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        db_table = 'gis_pref'
        default_permissions = ()
        ordering = ('pref_code',)
        verbose_name = "都道府県"
        verbose_name_plural = "都道府県一覧"

    def __str__(self):
        return self.pref_name


class City(BaseModel):
    pref = models.ForeignKey(Pref, db_column='pref_code', on_delete=models.PROTECT, verbose_name="都道府県番号")
    pref_name = models.CharField(max_length=20, verbose_name="都道府県名称")
    city_code = models.CharField(max_length=5, primary_key=True, verbose_name="市区町村番号")
    city_name = models.CharField(max_length=30, verbose_name="市区町村名称")
    city_name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name="市区町村名称（英語）")
    gun_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="郡名（町村部のみ）")
    people_count = models.IntegerField(blank=True, null=True, verbose_name="人口")
    family_count = models.IntegerField(blank=True, null=True, verbose_name="世帯数")
    mpoly = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        db_table = 'gis_city'
        indexes = (
            models.Index(fields=('city_code',)),
            models.Index(fields=('city_name',)),
        )
        default_permissions = ()
        ordering = ('city_code',)
        verbose_name = "市区町村"
        verbose_name_plural = "市区町村一覧"

    def __str__(self):
        return self.city_name


# class Town(BaseModel):
#     code = models.CharField(max_length=12, verbose_name="大字町丁目コード")
#     name = models.CharField(max_length=30, verbose_name="大字町丁目名称")
#     city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="市区町村")
#     pref = models.ForeignKey(Pref, on_delete=models.PROTECT, verbose_name="都道府県")
#     point = models.PointField(blank=True, null=True, verbose_name="座標")
#     full_name = models.CharField(max_length=120, verbose_name="名称")
#     mpoly = models.MultiPolygonField(srid=4326, blank=True, null=True)
#     people_count = models.IntegerField(blank=True, null=True, verbose_name="人口")
#     family_count = models.IntegerField(blank=True, null=True, verbose_name="世帯数")
#
#     class Meta:
#         db_table = 'gis_town'
#         indexes = (
#             models.Index(fields=('code',)),
#             models.Index(fields=('name',)),
#         )
#         default_permissions = ()
#         ordering = ('code',)
#         verbose_name = "大字町丁目"
#         verbose_name_plural = "大字町丁目一覧"
#
#     def __str__(self):
#         return self.name


class Chome(BaseModel):
    pref = models.ForeignKey(Pref, db_column='pref_code', on_delete=models.PROTECT, verbose_name="都道府県番号")
    pref_name = models.CharField(max_length=20, verbose_name="都道府県名称")
    city = models.ForeignKey(City, db_column='city_code', on_delete=models.PROTECT, verbose_name="市区町村番号")
    city_name = models.CharField(max_length=20, verbose_name="市区町村名称")
    chome_code = models.CharField(max_length=12, verbose_name="大字町丁目番号")
    chome_name = models.CharField(max_length=30, verbose_name="大字町丁目名称")
    category = models.IntegerField(blank=True, null=True, choices=constants.CHOICE_CHOME_CATEGORY, verbose_name="分類コード")
    special_symbol_e = models.CharField(max_length=5, blank=True, null=True, verbose_name="特殊記号E（町丁・字等重複フラグ）")
    area = models.IntegerField(blank=True, null=True, verbose_name="面積（㎡）")
    perimeter = models.IntegerField(blank=True, null=True, verbose_name="周辺長（ｍ）")
    area_max_f = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="面積最大フラグ",
        help_text='一つの市区町村内に同一の町丁・字等番号を持つ境界が複数存在した場合、一番広い面積を持つ境界に付与。'
                  '又は、同一の町丁・字等番号を持つ境界がない場合に付与'
    )
    special_symbol_d = models.CharField(
        max_length=2, blank=True, null=True, choices=constants.CHOICE_SYMBOL_D, verbose_name="特殊記号D（飛び地、抜け地フラグ）"
    )
    people_count = models.IntegerField(blank=True, null=True, verbose_name="人口")
    family_count = models.IntegerField(blank=True, null=True, verbose_name="世帯数")
    center_lng = models.FloatField(blank=True, null=True, verbose_name="図形中心点経度")
    center_lat = models.FloatField(blank=True, null=True, verbose_name="図形中心点緯度")
    mpoly = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        db_table = 'gis_chome'
        indexes = (
            models.Index(fields=('chome_code',)),
            models.Index(fields=('chome_name',)),
        )
        default_permissions = ()
        ordering = ('chome_code',)
        verbose_name = "大字町丁目"
        verbose_name_plural = "大字町丁目一覧"

    def __str__(self):
        return self.chome_name


class Postcode(BaseModel):
    city_code = models.CharField(
        max_length=5, validators=(RegexValidator(regex=r"^\d{5}$"),), verbose_name=u"市区町村コード"
    )
    post_code = models.CharField(
        max_length=7, validators=(RegexValidator(regex=constants.REG_POST_CODE),), verbose_name=u"郵便番号"
    )
    pref_name = models.CharField(max_length=15, verbose_name="都道府県名称")
    pref_kana = models.CharField(max_length=50, verbose_name="度道府県カナ")
    city_name = models.CharField(max_length=50, verbose_name="市区町村名称")
    city_kana = models.CharField(max_length=50, verbose_name="市区町村カナ")
    town_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="町域名称")
    town_kana = models.CharField(max_length=100, blank=True, null=True, verbose_name="町域カナ")
    chome_list = models.CharField(
        max_length=200, blank=True, null=True,
        validators=[validate_comma_separated_integer_list], verbose_name="丁目リスト"
    )
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
        indexes = [models.Index(fields=['post_code']),]
        default_permissions = ()
        verbose_name = "郵便番号"
        verbose_name_plural = '郵便番号一覧'

    def __str__(self):
        return self.post_code

    @property
    def address(self):
        return "{}{}{}".format(self.pref_name, self.city_name, self.town_name or '')
