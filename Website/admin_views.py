from flask import request, Blueprint, render_template, flash
from .models import Upload_About_Carousel_Image, Upload_About_Cards_Image
from . import database
import os

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/admin-views', methods=['GET', 'POST'])
def admin_control():

    if request.method == 'POST':
        target_action = request.form.get('target_selection')
        file = request.files['file']

        if file.filename != '':
            end_point = 'static'
            current_dir = os.path.abspath(os.getcwd())
            root_folder_path = os.path.join(current_dir, 'Website')
            
            if target_action == "carousel_slide":
                end_point = os.path.join(end_point, 'resources\carousel_img')
                root_folder_path = os.path.join(root_folder_path, end_point)

                file.save(os.path.join(root_folder_path, file.filename))
                upload = Upload_About_Carousel_Image(filename=file.filename, image_dir=os.path.join(end_point, file.filename))
                database.session.add(upload)
                database.session.commit()

                flash("Image " + file.filename + " uploaded.", category='success')


            elif target_action  == "cards_image":
                end_point = os.path.join(end_point, 'resources\cards_img')
                root_folder_path = os.path.join(root_folder_path, end_point)

                card_position = request.form.get('card_position')
                text = request.form.get('content_text')

                check_image_in_use = Upload_About_Cards_Image.query.filter_by(filename = file.filename).first()
                
                if check_image_in_use == None:
                    check_card_position = Upload_About_Cards_Image.query.filter_by(target = card_position).first()

                    if check_card_position != None:
                        #image_delete = os.path.join(root_folder_path, Test.filename)
                        #flash(image_delete, category='success')

                        os.remove(os.path.join(root_folder_path, check_card_position.filename))
                        database.session.delete(check_card_position)
                        database.session.commit()

                    file.save(os.path.join(root_folder_path, file.filename))
                    upload = Upload_About_Cards_Image(filename=file.filename, text=text, target=card_position, image_dir=os.path.join(end_point, file.filename))
                    database.session.add(upload)
                    database.session.commit()

                    flash("Image " + file.filename + " uploaded.", category='success')
                else:
                     flash('Image already exist. Please rename or choose another image.', category='error')
    

        else :
            flash('Please select a image.', category='error')
        

    return render_template("admin_control_page.html")