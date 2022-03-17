

import flask

bdhcue = flask.Blueprint('bdhcue', __name__)

@bdhcue.route('/bdhcue', methods=['GET']) 
def bdhcue_hello():
    return flask.jsonify({"message": "lista hcue publicadas"})
    