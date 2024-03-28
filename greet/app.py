from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"




#export FLASK_ENV=development FLASK_DEBUG=1 flask run