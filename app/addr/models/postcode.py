from app.addr.models import db


class Postcode(db.Model):
    __tablename__ = 'gis_post_code'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_code = db.Column(db.String(7), nullable=False)
    pref_code = db.Column(db.String(2), nullable=False)
    pref_name = db.Column(db.String(15), nullable=False)
    pref_kana = db.Column(db.String(50), nullable=False)
    city_code = db.Column(db.String(5), nullable=False)
    city_name = db.Column(db.String(50), nullable=False)
    city_kana = db.Column(db.String(50), nullable=False)
    town_name = db.Column(db.String(50), nullable=True)
    town_kana = db.Column(db.String(100), nullable=True)
    chome_list = db.Column(db.String(200), nullable=True)
    is_partial = db.Column(db.Boolean)
    is_multi_chome = db.Column(db.Boolean)
    is_multi_town = db.Column(db.Boolean)

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
