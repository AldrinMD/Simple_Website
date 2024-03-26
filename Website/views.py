from flask import Blueprint, render_template, request,flash
from .models import Upload_About_Image


views = Blueprint('views', __name__)

@views.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        images = Upload_About_Image.query.filter(Upload_About_Image.target == 'carousel_slide').all()

        # User is the name of table that has a column name
        # users = User.query.all()
        #flash(images, category='error')

    return render_template("about.html", image=images)