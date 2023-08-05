from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import os



INDIA = "india"
GERMANY = "germany"
SPAIN = "spain"
POST = "POST"
GET = "GET"
UPLOAD_DIR = "uploads"


app = Flask(__name__)

@app.route('/')
def homepage():
    return "Flask Homepage"

@app.route('/intro/<string:name>')
def intoduction(name):    
    return "Hello " + str(name).capitalize()


@app.route("/india")
def greet_india():
    return "Namaste!"


@app.route("/germany/<city>")
def greet_germany(city):
    return "Hallo!" + " from " + city

@app.route("/spain")
def greet_spain():
    return "Hola!"


@app.route('/user/<country>')
def display_country_info(country):
    country = str(country).lower()
    if country == INDIA:
        return redirect(url_for('greet_india'))
    elif country == GERMANY:
        return redirect(url_for('greet_germany', city="Munich"))
    elif country == SPAIN:
        return redirect(url_for('greet_spain'))
    
    return "Invalid : " + country


@app.route('/success/<name>')
def success(name):
    return f"<html><body><h1>Welcome : {str(name).capitalize()}</h1></body></html>"


@app.route('/login', methods=[POST, GET])
def login():
    if request.method == POST:
        user = request.form["nm"]
        return redirect(url_for('success', name = user))
    else:
        #return render_template('login.html')
        user = request.args.get("nm")
        return redirect(url_for('success', name = user))
    

@app.route('/upload')
def upload_view():
    return render_template('upload.html')


@app.route('/uploader', methods=[GET, POST])
def upload_file():
    if request.method == POST:
        file = request.files['file']
        # Make upload directory if it isn't there
        # Can also use app.instance_path
        os.makedirs(os.path.join(app.root_path, UPLOAD_DIR), exist_ok=True)        
        file.save(os.path.join(app.root_path, UPLOAD_DIR, secure_filename(file.filename)))
        return "File uploaded successfully."


if __name__ == "__main__":
    app.run(debug=True)