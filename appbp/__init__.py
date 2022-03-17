#config bp-routes

from flask import Flask
import flask

from appbp.registerp import registerp_routes

from .landingp import landingp
from .loginp import loginp
from .registerp import registerp


app = flask.Flask(__name__)

app.config.from_pyfile('config/config.cfg')
app.register_blueprint(landingp)
app.register_blueprint(loginp)
app.register_blueprint(registerp)

