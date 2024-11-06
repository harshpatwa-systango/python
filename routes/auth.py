# routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db, bcrypt  # Import from extensions
from flask_login import login_user
from models.user import User
from flask_login import logout_user

auth_bp = Blueprint('auth', __name__)

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('user.home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')

    return render_template('login.html')

# Signup route
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

# Logout route
@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
