from flask import Blueprint, render_template, request,flash
from .models import Upload_Image


views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        images = Upload_Image.query.filter_by(target = 'carousel_slide_1').first()

        # User is the name of table that has a column name
        # users = User.query.all()


    return render_template("homepage.html", image=images)