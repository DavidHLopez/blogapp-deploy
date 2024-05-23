
from flask import request, render_template


from . import landingp 




@landingp.route('/', methods=['GET'])
def home():
    return render_template('landingp_index.html')

@landingp.route('/s01a01', methods=['GET'])
def reg1():
    return render_template('s01a01.html')

@landingp.route('/s01a02', methods=['GET'])
def reg2():
    return render_template('s01a02.html')

@landingp.route('/s01a03', methods=['GET'])
def reg3():
    return render_template('s01a03.html')

@landingp.route('/s01a04', methods=['GET'])
def reg4():
    return render_template('s01a04.html')

@landingp.route('/s01a05', methods=['GET'])
def reg5():
    return render_template('s01a05.html')

@landingp.route('/RIPSPR', methods=['GET'])
def reg6():
    return render_template('RIPSPR.html')

@landingp.route('/RDA', methods=['GET'])
def reg():
    return render_template('RDA.html')





