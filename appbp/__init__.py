#config bp-routes

from flask import Flask
from flask_cors import CORS



from .landingp import landingp

from .articles import articles


app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config/config.cfg')

app.register_blueprint(landingp)

app.register_blueprint(articles)

