from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Task
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        description=data['description'],
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'description': task.description, 'due_date': task.due_date.strftime('%Y-%m-%d')} for task in tasks])

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({'id': task.id, 'description': task.description, 'due_date': task.due_date.strftime('%Y-%m-%d')})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    task = Task.query.get_or_404(id)
    task.description = data['description']
    task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
