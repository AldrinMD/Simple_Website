from flask import Blueprint, render_template, request,flash
from .models import Upload_About_Carousel_Image


views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template("homepage.html")

@views.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        #images = Upload_About_Carousel_Image.query.filter(Upload_About_Carousel_Image.target == 'carousel_slide').all()
        images = Upload_About_Carousel_Image.query.all()

        # User is the name of table that has a column name
        # users = User.query.all()
        #flash(images, category='error')

    return render_template("about.html", image=images)