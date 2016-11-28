"""
Tutorial : https://www.digitalocean.com/community/tutorials/how-to-use-the-bottle-micro-framework-to-develop-python-web-apps
"""

import sqlite3, bottle
from bottle import route, run, template, response, request 


""" Handle the CORS Issues """
# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

app = bottle.app()


''' Router Definition '''

# Basic response
@app.route('/hello')
def hello():
    return "Hello Hippo!"


# Basic DB query example
@app.route('/picnic')
def show_picnic():
    db = sqlite3.connect('picnic.db')
    c = db.cursor()
    c.execute("SELECT item,quant FROM picnic")
    data = c.fetchone()
    c.close()
    print data
    return template('Hello {{name}}, how are you?', name=data[0])


# Response some messages in dictionary to client app
@app.route('/getResponse', method=['OPTIONS', 'POST'])
@enable_cors
def responseStr():

    print "Http Request /getResponse - input :"
    print "==================================="
    print request.json['description']
    print "==================================="

    res = {
        'firstStrList': ['I', 'love', 'Sherry.'],
        'secondStrList': ['Sherry', 'loves', 'me.']
    }
    
    return res



# Response some messages in dictionary to client app
@app.route('/queryDB', method=['OPTIONS', 'POST'])
@enable_cors
def queryPicnic():
    
    print "Http Request /getResponse - input :"
    print "==================================="
    print request.json['description']
    print "==================================="

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute("SELECT * FROM Employee")
    dataFromDB = c.fetchall()
    c.close()
    #print dataFromDB

    res = {
        'firstStrList': [dataFromDB[0][0],dataFromDB[0][1]]
        
    }
    #print res
    
    return res

# Response some messages in dictionary to client app
@app.route('/sendForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendForm():

    print "Http Request /sendForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="

    res = {
        'message': "Hi, %s %s. You send this form successfully!" % (inputData['first_name'], inputData['last_name']),
    }
    
    return res


@app.route('/sendCusForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendCusForm():
    print "Http Request /sendCusForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'

    print info
    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()

    res ={
      'message': "You send this form successfully!",
    }

    return res





''' Start the server '''
try:
    app.run(host='localhost', port=7000, debug=True, reloader=True)
except KeyboardInterrupt:
    # never reached
    print('exiting...')
