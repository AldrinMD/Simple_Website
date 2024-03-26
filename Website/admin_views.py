from flask import request, Blueprint, render_template, flash
from .models import Upload_About_Image
from . import database
import os

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/admin-views', methods=['GET', 'POST'])
def admin_control():

    if request.method == 'POST':
        target_action = request.form.get('target_selection')
        file = request.files['file']

        if file != '':
            end_point = 'static'
            text = ""
            
            if target_action == "carousel_slide":
                end_point = os.path.join(end_point, 'resources\carousel_img')

            current_dir = os.path.abspath(os.getcwd())
            root_folder_path = os.path.join(current_dir, 'Website')
            root_folder_path = os.path.join(root_folder_path, end_point)

            file.save(os.path.join(root_folder_path, file.filename))
            upload = Upload_About_Image(filename=file.filename, text = text, data_type=file.mimetype, target=target_action, image_dir=os.path.join(end_point, file.filename))
            database.session.add(upload)
            database.session.commit()

        else :
            flash('Please select a image.', category='error')
        

    return render_template("admin_control_page.html")