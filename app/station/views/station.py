from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from ..models.station import Station

station = Blueprint('station', __name__, url_prefix='/api/station/stations')


@station.route('/', methods=['GET'])
@cross_origin()
def search_station():
    q = request.args.get('q', None)
    if q:
        records = Station.query.filter(Station.station_name.like('{}%'.format(q))).limit(10)
    else:
        records = []
    return jsonify([r.to_json() for r in records]), 200
