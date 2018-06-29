from flask import Flask, render_template, request, make_response, session
app = Flask(__name__)
app.secret_key = 'secrety-secret'
@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('index-cookie.html'))
        session['userID'] = user
        return resp
    return make_response(render_template('index-cookie.html'))

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('index-cookie.html'))
        session['userID'] = user
    return '<h1>Cookie set!</h1><a href="/getcookie">See your cookie!</a>'

@app.route('/getcookie', methods=['POST', 'GET'])
def getcookie():
   name = session['userID']
   return '<h1>welcome '+str(name)+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)
