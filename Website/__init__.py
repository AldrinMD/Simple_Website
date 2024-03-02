from flask import Flask

def initialize_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = 'DEV KEY'

    from.views import views
    from.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app