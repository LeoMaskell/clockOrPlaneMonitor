from flask import *

app = Flask(__name__)

@app.route("/")
def heyup():
    return "<h1> hello world </h1>"