from flask import Flask, render_template, request, make_response
app = Flask(__name__)
app.secret_key = 'secrety-secret'

@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('index-cookie.html'))
        resp.set_cookie('userID', user)
        return resp
    return make_response(render_template('index-cookie.html'))

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    user = request.form['nm']
    resp = make_response(render_template('index-cookie.html'))
    resp.set_cookie('userID', user)
    return '<h1>Cookie set!</h1><a href="/getcookie">See your cookie!</a>'

@app.route('/getcookie', methods=['POST', 'GET'])
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+str(name)+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)
