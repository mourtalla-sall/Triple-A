from flask import Flask,render_template
from .data_api import data_api
app = Flask(__name__)

app.register_blueprint(data_api)
@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/dashboard")
def render_dashboard():
    return render_template("dashboard.html")

def build_app():
    return app

