import pytest
from flask import session
from app import app as flask_app
from io import BytesIO

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<body>" in response.data

def test_upload(client):
    response = client.get('/upload')
    assert response.status_code == 200
    assert b"<body>" in response.data

def test_cargar(client):
    response = client.post('/cargar', data={'file': (BytesIO(b'my file contents'), 'test.txt')})
    assert response.status_code == 200
    assert b"<body>" in response.data

def test_ask(client):
    response = client.post('/ask', data={'question': 'test question'})
    assert response.status_code == 302
    assert session['prompt'] == 'test question'