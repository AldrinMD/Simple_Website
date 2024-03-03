from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import database

auth = Blueprint('auth', __name__)

@auth.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        signup_email = request.form.get('signup_email').lower()
        signup_firstName = request.form.get('signup_firstName').lower()
        signup_lastName = request.form.get('signup_lastName').lower()
        signup_password = request.form.get('signup_password')
        signup_confirmPassword = request.form.get('signup_confirmPassword')

        user = User.query.filter_by(email = signup_email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(signup_email) < 5:
            flash('Email must be greater than 5 characters. Please try again.', category='error')
        elif len(signup_firstName) < 2:
            flash('First name must be greater than 2 characters. Please try again.', category='error')
        elif len(signup_lastName) < 2:
            flash('Last name must be greater than 2 characters. Please try again.', category='error')
        elif len(signup_password) < 6:
            flash('Password must be greater than 6 characters. Please try again.', category='error') 
        elif not any(char.isdigit() for char in signup_password):
            flash('Password must contain a number. Please try again.', category='error') 
        elif not any(char.isupper() for char in signup_password):
            flash('Password must contain a capital letter. Please try again.', category='error') 
        elif signup_password != signup_confirmPassword:
            flash('Password doesn\'t match. Please try again.', category='error')
        else:
            new_User = User(email = signup_email, first_name = signup_firstName, last_name = signup_lastName, password = generate_password_hash(signup_password, method="sha256"))
            database.session.add(new_User)
            database.session.commit()

            user = User.query.filter_by(email = signup_email).first()
            if user:
                if check_password_hash(user.password, signup_password):

                    flash('Account successfully created', category='success')
                    return redirect(url_for('views.home'))
    
    return render_template("register.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('login_email').lower()
        password = request.form.get('login_password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successfully logged in.', category='success')
                login_user(user, remember = True)
                return redirect(url_for('views.home'))
            else:
                flash('Login failed.', category='error')
        else:
            flash('Email not found.', category='error')
    
    return render_template("login.html", user = current_user)

@auth.route('/logout')
def logout():
    return render_template("homepage.html")