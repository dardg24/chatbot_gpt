import requests
import pytest
from app import app

def test_index_endpoint():
    url = 'http://localhost:5000/'  
    response = requests.get(url)
    assert response.status_code == 200
    assert "Texto específico de index.html" in response.text

def test_upload_endpoint():
    url = 'http://localhost:5000/upload'  
    response = requests.get(url)
    assert response.status_code == 200
    assert "Texto específico de template1.html" in response.text

# Aquí necesitarías un archivo de texto para probar este endpoint
def test_cargar_endpoint():
    url = 'http://localhost:5000/cargar'
    files = {'file': open('test.txt', 'rb')}
    response = requests.post(url, files=files)
    assert response.status_code == 200
    assert "Texto específico de template2.html" in response.text

# Aquí necesitarías proporcionar un prompt para probar este endpoint
def test_ask_endpoint():
    url = 'http://localhost:5000/ask'
    data = {'question': 'test prompt'}
    response = requests.post(url, data=data)
    assert response.status_code == 302  # Redirección a 'resumen'

def test_resumen_endpoint():
    url = 'http://localhost:5000/resumen'
    response = requests.get(url)
    assert response.status_code == 200
    assert "Texto específico de template3.html" in response.text

def test_consulta_endpoint():
    url = 'http://localhost:5000/consulta'
    response = requests.get(url)
    assert response.status_code == 200