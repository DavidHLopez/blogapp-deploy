

from flask import request, render_template
from pymongo import MongoClient

from . import registerp


#mongoclient 

client= MongoClient(port=27017)

#db name

db = client.profuser_data


@registerp.route('/register', methods=['POST'])

def data():
    data ={}
    if request.method == "POST":
        data['Name'] = request.form ['name']
        data['DNI'] = request.form ['dni']
        data['Email'] = request.form ['email']
        data['FN'] = request.form ['fn']
        data['Gender'] = request.form ['gender']
        data['Telefono'] = request.form ['telefono']
        prof = []
        for i in "1234567":
            try:
                if request.form['profesional' + i] != "":
                    prof.append(request.form['profesional' + i])
            except Exception as e:
                pass
        data['Profesional'] = prof
        db.profuserData.insert_one(data)
        return render_template('contact_response.html')



