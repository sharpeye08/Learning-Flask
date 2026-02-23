from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello user! This is my first flask app."

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "This is a contact us page"

