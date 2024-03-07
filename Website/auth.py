from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import database

auth = Blueprint('auth', __name__)

@auth.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_email = request.form.get('register_email').lower()
        register_firstName = request.form.get('register_firstName').lower()
        register_lastName = request.form.get('register_lastName').lower()
        register_password = request.form.get('register_password')
        register_confirmPassword = request.form.get('register_confirmPassword')

        user = User.query.filter_by(email = register_email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(register_email) < 5:
            flash('Email must be greater than 5 characters. Please try again.', category='error')
        elif len(register_firstName) < 2:
            flash('First name must be greater than 2 characters. Please try again.', category='error')
        elif len(register_lastName) < 2:
            flash('Last name must be greater than 2 characters. Please try again.', category='error')
        elif len(register_password) < 6:
            flash('Password must be greater than 6 characters. Please try again.', category='error') 
        elif not any(char.isdigit() for char in register_password):
            flash('Password must contain a number. Please try again.', category='error') 
        elif not any(char.isupper() for char in register_password):
            flash('Password must contain a capital letter. Please try again.', category='error') 
        elif register_password != register_confirmPassword:
            flash('Password doesn\'t match. Please try again.', category='error')
        else:
            new_User = User(email = register_email, first_name = register_firstName, last_name = register_lastName, password = generate_password_hash(register_password, method="sha256"))
            database.session.add(new_User)
            database.session.commit()

            user = User.query.filter_by(email = register_email).first()
            if user:
                if check_password_hash(user.password, register_password):

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