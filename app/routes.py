from flask import Blueprint, request, jsonify
from .models import db, Task
from datetime import datetime
import pytz

bp = Blueprint('api', __name__)
TEHRAN = pytz.timezone('Asia/Tehran')

@bp.route('/tasks', methods=['GET'])
def get_all():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])


@bp.route('/tasks', methods=['POST'])
def create():
    data = request.get_json()
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status='pending'
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@bp.route('/tasks/<int:id>', methods=['PUT'])
def update(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    
    if task.status != 'pending':
        return jsonify({"error": "نمی‌تونی وظیفه انجام‌شده یا کنسل‌شده رو ویرایش کنی"}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:id>/status', methods=['PATCH'])
def change_status(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    new_status = data.get('status')

    if new_status not in ['done', 'canceled']:
        return jsonify({"error": "وضعیت نامعتبر"}), 400

    task.status = new_status
    if new_status == 'done':
        task.completed_at = datetime.now(TEHRAN)
    else:  # canceled
        task.completed_at = None
    task.updated_at = datetime.now(TEHRAN)
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204