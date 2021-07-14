from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from ...addr.models.area import Pref
from ...utils import constants
from ...utils.base_model import ChoiceType, BaseModel


class Company(BaseModel):
    __tablename__ = 'gis_railway_company'

    company_code = Column(Integer, primary_key=True, comment='事業者コード')
    railway_code = Column(Integer, nullable=False, comment='鉄道コード')
    company_name = Column(String(80), nullable=False, comment='事業者名')
    company_kana = Column(String(80), nullable=True, comment='事業者カナ')
    company_full_name = Column(String(80), nullable=True, comment='事業者名(正式名称)')
    company_short_name = Column(String(80), nullable=True, comment='事業者名(略称)')
    company_url = Column(String(100), nullable=True, comment='Webサイト')
    company_type = Column(ChoiceType(constants.CHOICE_STATION_COMPANY_TYPE), nullable=True, comment='事業者区分')
    status = Column(ChoiceType(constants.CHOICE_STATION_STATUS), nullable=True, comment='状態')


class Route(BaseModel):
    __tablename__ = 'gis_railway_route'

    line_code = Column(Integer, primary_key=True, comment='路線コード(整数5桁　鉄道コード + エリアコード + 連番　※新幹線は4桁)')
    company_code = Column(
        'company_code', Integer,
        ForeignKey(Company.company_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="事業者コード"
    )
    company = relationship(Company)
    line_name = Column(String(80), comment="路線名称")
    line_kana = Column(String(80), comment="路線カナ")
    line_full_name = Column(String(80), nullable=True, comment="路線名称(正式名称)")
    color_code = Column(String(6), nullable=True, comment="路線カラーコード")
    color_name = Column(String(10), nullable=True, comment="路線カラー名称")
    line_type = Column(ChoiceType(constants.CHOICE_STATION_LINE_TYPE), nullable=True, comment="路線区分")
    center_lng = Column(Float, nullable=True, comment="路線表示時の中央経度")
    center_lat = Column(Float, nullable=True, comment="路線表示時の中央緯度")
    zoom = Column(Integer, nullable=True, comment="路線表示時のGoogleMap倍率")
    status = Column(ChoiceType(constants.CHOICE_STATION_STATUS), nullable=True, comment="状態")


class Station(BaseModel):
    __tablename__ = 'gis_station'

    station_code = Column(Integer, primary_key=True, comment="駅コード(整数7桁 ※新幹線は6桁)")
    station_group_code = Column(Integer, comment="駅グループコード")
    station_name = Column(String(80), comment="駅名称")
    station_kana = Column(String(80), nullable=True, comment="駅カナ")
    station_name_en = Column(String(80), nullable=True, comment="駅カナ")
    line_code = Column(
        'line_code', Integer,
        ForeignKey(Route.line_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="路線"
    )
    route = relationship(Route)
    pref_code = Column(
        'pref_code', String(2),
        ForeignKey(Pref.pref_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="都道府県コード"
    )
    pref = relationship(Pref)
    post_code = Column(String(8), nullable=True, comment="駅郵便番号")
    address = Column(String(300), nullable=True, comment="住所")
    lng = Column(Float, nullable=True, comment="経度")
    lat = Column(Float, nullable=True, comment="緯度")
    point = Column(Geometry(geometry_type='POINT', dimension=2, srid=4326), nullable=True, comment='座標')
    open_date = Column(Date, nullable=True, comment="開業年月日")
    close_date = Column(Date, nullable=True, comment="廃止年月日")
    status = Column(ChoiceType(constants.CHOICE_STATION_STATUS), nullable=True, comment="状態")

    def to_json(self):
        return {
            'station_code': self.station_code,
            'station_name': self.station_name,
            'lng': self.lng,
            'lat': self.lat,
            'pref_code': self.pref_code,
            'pref_name': self.pref.pref_name,
        }


class JoinStation(BaseModel):
    __tablename__ = 'gis_join_station'

    id = Column(Integer, primary_key=True, autoincrement=True)
    line_code = Column(
        'line_code', Integer,
        ForeignKey(Route.line_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="路線コード"
    )
    route = relationship(Route)
    station_code1 = Column(
        Integer,
        ForeignKey(Station.station_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="駅コード１"
    )
    station1 = relationship(Station, foreign_keys=(station_code1,))
    station_code2 = Column(
        Integer,
        ForeignKey(Station.station_code, onupdate='CASCADE', ondelete='RESTRICT'),
        comment="駅コード２"
    )
    station2 = relationship(Station, foreign_keys=(station_code2,))
