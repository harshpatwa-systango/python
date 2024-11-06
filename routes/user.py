# routes/user.py

from flask import Blueprint, render_template
from extensions import db  # Import from extensions
from models.user import User

user_bp = Blueprint('user', __name__)

# Home route (protected)
@user_bp.route('/')
def home():
    return render_template('home.html')

# Route to view all users
@user_bp.route('/users')
def all_users():
    users = User.query.all()  # Fetch all users from the database
    return render_template('users.html', users=users)
