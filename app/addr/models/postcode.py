from sqlalchemy import Column, Integer, String, Boolean

from ...utils.base_model import BaseModel


class Postcode(BaseModel):
    __tablename__ = 'gis_post_code'

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_code = Column(String(7), nullable=False)
    pref_code = Column(String(2), nullable=False)
    pref_name = Column(String(15), nullable=False)
    pref_kana = Column(String(50), nullable=False)
    city_code = Column(String(5), nullable=False)
    city_name = Column(String(50), nullable=False)
    city_kana = Column(String(50), nullable=False)
    town_name = Column(String(50), nullable=True)
    town_kana = Column(String(100), nullable=True)
    chome_list = Column(String(200), nullable=True)
    is_partial = Column(Boolean)
    is_multi_chome = Column(Boolean)
    is_multi_town = Column(Boolean)

    @property
    def address(self):
        return "{}{}{}".format(self.pref_name, self.city_name, self.town_name or '')

    def to_json(self):
        return {
            'id': self.id,
            'post_code': self.post_code,
            'pref_code': self.pref_code,
            'pref_name': self.pref_name,
            'city_code': self.city_code,
            'city_name': self.city_name,
            'town_name': self.town_name,
            'address': self.address,
        }
