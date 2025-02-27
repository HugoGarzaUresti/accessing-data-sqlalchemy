from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
