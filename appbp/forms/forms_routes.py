

from flask import request, render_template


from . import forms




@forms.route('/', methods=['GET'])

def data():
        if request.method == "GET":
            return render_template('landingp_index.html')



