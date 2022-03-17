

import flask

forms = flask.Blueprint('forms', __name__)

@forms.route('/forms', methods=['GET']) 
def forms_hello():
    return flask.jsonify({"message": " Forms listado de formularios"})
    