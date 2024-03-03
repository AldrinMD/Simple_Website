from . import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    email = database.Column(database.String(150), unique = True)
    first_name = database.Column(database.String(150))
    last_name = database.Column(database.String(150))
    password = database.Column(database.String(150))