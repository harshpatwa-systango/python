from flask import Flask
from config import Config
from routes.auth import auth_bp
from routes.user import user_bp
from extensions import db, bcrypt, login_manager  

# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize the extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')

# User loader function for Flask-Login
from models.user import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
