from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from ...utils import constants
from ...utils.base_model import BaseModel, IntChoiceType, ChoiceType


class Pref(BaseModel):
    __tablename__ = 'gis_pref'

    pref_code = Column(String(2), primary_key=True, comment="都道府県番号")
    pref_name = Column(String(20), comment="都道府県名称")
    people_count = Column(Integer, nullable=True, comment="人口")
    family_count = Column(Integer, nullable=True, comment="世帯数")
    mpoly = Column(Geometry(geometry_type='MULTIPOLYGON', dimension=2, srid=4326), nullable=True)


class City(BaseModel):
    __tablename__ = 'gis_city'

    pref_code = Column(
        'pref_code', String(2),
        ForeignKey(Pref.pref_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="都道府県番号"
    )
    pref = relationship(Pref)
    pref_name = Column(String(20), comment="都道府県名称")
    city_code = Column(String(5), primary_key=True, comment="市区町村番号")
    city_name = Column(String(30), comment="市区町村名称")
    city_name_en = Column(String(50), nullable=True, comment="市区町村名称（英語）")
    gun_name = Column(String(30), nullable=True, comment="郡名（町村部のみ）")
    people_count = Column(Integer, nullable=True, comment="人口")
    family_count = Column(Integer, nullable=True, comment="世帯数")
    mpoly = Column(Geometry(geometry_type='MULTIPOLYGON', dimension=2, srid=4326), nullable=True)


class Town(BaseModel):
    __tablename__ = 'gis_town'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pref_code = Column(
        'pref_code', String(2),
        ForeignKey(Pref.pref_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="都道府県番号"
    )
    pref = relationship(Pref)
    pref_name = Column(String(20), comment="都道府県名称")
    city_code = Column(
        'city_code', String(5),
        ForeignKey(City.city_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="市区町村番号"
    )
    city = relationship(City)
    city_name = Column(String(20), comment="市区町村名称")
    town_code = Column(String(12), comment="大字町丁目番号")
    town_name = Column(String(30), comment="大字町丁目名称")
    category = Column(IntChoiceType(constants.CHOICE_CHOME_CATEGORY), nullable=True, comment="分類コード")
    special_symbol_e = Column(String(5), nullable=True, comment="特殊記号E（町丁・字等重複フラグ）")
    area = Column(Integer, nullable=True, comment="面積（㎡）")
    perimeter = Column(Integer, nullable=True, comment="周辺長（ｍ）")
    # 一つの市区町村内に同一の町丁・字等番号を持つ境界が複数存在した場合、一番広い面積を持つ境界に付与。
    # 又は、同一の町丁・字等番号を持つ境界がない場合に付与
    area_max_f = Column(String(1), nullable=True, comment="面積最大フラグ")
    special_symbol_d = Column(ChoiceType(constants.CHOICE_SYMBOL_D), nullable=True, comment="特殊記号D（飛び地、抜け地フラグ）")
    people_count = Column(Integer, nullable=True, comment="人口")
    family_count = Column(Integer, nullable=True, comment="世帯数")
    center_lng = Column(Float, nullable=True, comment="図形中心点経度")
    center_lat = Column(Float, nullable=True, comment="図形中心点緯度")
    mpoly = Column(Geometry(geometry_type='MULTIPOLYGON', dimension=2, srid=4326), nullable=True)
