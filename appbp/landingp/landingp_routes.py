
from flask import request, render_template
from pymongo import MongoClient 

from . import landingp 

#mongoclient 

client= MongoClient(port=27017)

#db name

db = client.contact_data


@landingp.route('/', methods=['GET'])
def home():
    return render_template('landingp_index.html')

@landingp.route('/register', methods=['GET'])
def reg():
    return render_template('registerp_index.html')

@landingp.route( '/contactr', methods=['POST'])

def data(): 
    data = {}
    if request.method == "POST": 
        data['Name'] = request.form ['name']
        data['Email']= request.form ['email']
        data['Message'] = request.form ['message']
        db.contactData.insert_one(data) 
        return render_template('contact_response.html')








