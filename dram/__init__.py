from flask import Flask, Blueprint, render_template

from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap


frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('welcome.html')


def create_app(configfile=None):
    app = Flask(__name__)

    AppConfig(app)
    Bootstrap(app)

    app.register_blueprint(frontend)

    return app
