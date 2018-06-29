#!/usr/bin/python
from flask import Flask, render_template, request, session, flash, redirect, url_for, logging, make_response

app = Flask(__name__, template_folder="templates")
app.secret_key = "AIzaSyC-jyfRJC7gRskgtLADyrOCod3EzhVYE7s"

@app.route('/')
def root():
    return redirect(url_for("chat"))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user = request.form["username"]
        msg = request.form["msg"]
        time = request.date

        session["msglog"].append((user,msg,time))
        return render_template('chat.html', msglog=session["msglog"])
    return render_template('chat.html', msglog=session["msglog"])

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)