from flask import Blueprint, jsonify
from flask_cors import cross_origin

from app.addr.models.postcode import Postcode

postcode = Blueprint('postcode', __name__, url_prefix='/api/addr/postcode')


@postcode.route('/<regex("[0-9]{7}"):code>', methods=['GET'])
@cross_origin()
def get_by_postcode(code):
    records = Postcode.query.filter_by(post_code=code)
    return jsonify([r.to_json() for r in records]), 200
