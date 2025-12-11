from flask import Flask,render_template
from .data_api import data_api
from .system_module.psutile_module import take_general_info
app = Flask(__name__)

app.register_blueprint(data_api)
@app.route("/")
def render_index():
    data = take_general_info()
    return render_template("index.html", data=data)

@app.route("/dashboard")
def render_dashboard():
    return render_template("dashboard.html")

def build_app():
    return app

