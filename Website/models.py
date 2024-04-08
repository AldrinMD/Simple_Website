from . import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    email = database.Column(database.String(150), unique = True)
    first_name = database.Column(database.String(150))
    last_name = database.Column(database.String(150))
    password = database.Column(database.String(150))

class Upload_About_Carousel_Image(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    filename = database.Column(database.String(50))
    image_dir = database.Column(database.String(150))

class Upload_About_Cards_Image(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    filename = database.Column(database.String(50))
    text = database.Column(database.String(150))
    target = database.Column(database.String(150))
    image_dir = database.Column(database.String(150))






'''
class Upload_About_Carousel_Image(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    filename = database.Column(database.String(50))
    text = database.Column(database.String(150))
    data_type = database.Column(database.String(50))
    target = database.Column(database.String(150))
    image_dir = database.Column(database.String(150))
'''