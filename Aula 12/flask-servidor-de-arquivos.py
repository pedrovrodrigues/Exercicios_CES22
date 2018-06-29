from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
app.secret_key = 'secrety-secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'newFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['newFile']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            session["archives"].append(filename)
            session.modified = True
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\','/'))
            return redirect(url_for('uploaded_file', filename=filename))
    if "archives" in session:
        listarc = session["archives"]
        return render_template('server.html', archives=listarc)
    else:
        session["archives"] = []
        return render_template('server.html', archives=[])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
   app.run(debug = True)
