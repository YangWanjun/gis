from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.routing import BaseConverter

from app.addr.models import db
from app.addr.views.postcode import postcode

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
CORS(app)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

app.register_blueprint(postcode)

db.init_app(app)
Migrate(app, db)


@app.route('/')
def index():
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
