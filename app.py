from flask import Flask, jsonify, request  # Import request here
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:macbook21@localhost:5432/flask_database"

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Corrected Integer
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)  # Corrected Column spelling

# Create tables if they don't exist (ideally, run this once, when setting up the app)
with app.app_context():
    db.create_all()

# Root route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route to get all tasks
@app.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title, 'done': task.done} for task in tasks]
    return jsonify({"tasks": task_list})

@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()  # Now request is defined
    new_task = Task(title=data['title'], done=data['done'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

if __name__ == '__main__':
    app.run(debug=True)
