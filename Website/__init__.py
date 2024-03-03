from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

database = SQLAlchemy()
DATABASE_NAME = "simple_website_database.db"

def initialize_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = 'DEV KEY'

    DATABASE_PATH = path.join(path.dirname(__file__), DATABASE_NAME)
    DATABASE_URI = 'sqlite:///{}'.format(DATABASE_PATH)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    database.init_app(app)

    from.views import views
    from.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('Website/' + DATABASE_NAME):
        with app.app_context():
            database.create_all()
        print('Created Database')