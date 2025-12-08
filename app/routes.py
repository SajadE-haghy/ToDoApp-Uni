from flask import Blueprint, request, jsonify
from .models import db, Task

bp = Blueprint('api', __name__)

@bp.route('/tasks', methods=['GET'])
def get_all():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])

@bp.route('/tasks', methods=['POST'])
def create():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@bp.route('/tasks/<int:id>', methods=['PUT'])
def update(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204