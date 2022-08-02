

from flask import request, render_template


from . import articles




@articles.route('/', methods=['GET'])

def data():
        if request.method == "GET":
            return render_template('index.html')



