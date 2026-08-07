from flask import *
from main import *
"""
print(f"coords:     {postcodeToLattLong('l24 1yd')}") # JLA airport for an example
print(in_radius(planes["states"], Liverpool, 5))
"""
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/info.html")
def info():
    return render_template("info.html")