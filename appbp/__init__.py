#config bp-routes

from flask import Flask
import flask



from .landingp import landingp

from .articles import articles


app = Flask(__name__)

app.config.from_pyfile('config/config.cfg')

app.register_blueprint(landingp)

app.register_blueprint(articles)

