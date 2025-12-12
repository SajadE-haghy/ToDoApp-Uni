import pytest
from app import create_app
from app.models import db, Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_crud(client):
    # Create
    rv = client.post('/api/tasks', json={'title': 'تست', 'description': 'توضیح'})
    assert rv.status_code == 201
    id = rv.json['id']

    # Read
    rv = client.get('/api/tasks')
    assert len(rv.json) == 1

    # Update status
    rv = client.patch(f'/api/tasks/{id}/status', json={'status': 'done'})
    assert rv.json['status'] == 'done'

    # Delete
    client.delete(f'/api/tasks/{id}')
    assert len(client.get('/api/tasks').json) == 0