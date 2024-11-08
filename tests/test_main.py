from fastapi.testclient import TestClient
from typing import Dict
from main import app
from models.models import Sheep

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert (response.json() ==
    {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    })

def test_add_sheep():
    new_sheep_data = {
        "id": 7,
        "name": "FirstSheep",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    response = client.post("/sheep", json=new_sheep_data)
    assert response.status_code == 201
    assert (response.json() == new_sheep_data)
    response_two = client.get("/sheep/7")
    assert response_two.status_code == 200
    assert (response_two.json() == new_sheep_data)

def test_delete_sheep():
    response = client.delete("/sheep/6")
    assert response.status_code == 200
    response_two = client.get("/sheep/6")
    assert response_two.status_code == 404

def test_update_sheep():
    new_sheep_data = {
        "id": 2,
        "name": "FirstSheep",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    response = client.put("/sheep", json=new_sheep_data)
    assert response.status_code == 200
    assert (response.json() == new_sheep_data)
    response_two = client.get("/sheep/2")
    assert response_two.status_code == 200
    assert (response_two.json() == new_sheep_data)