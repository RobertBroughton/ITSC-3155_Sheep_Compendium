from fastapi import FastAPI,HTTPException
from starlette import status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    if id in db.data:
        return db.get_sheep(id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")
    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}")
def delete_sheep(id: int):
    if id in db.data:
        db.delete_sheep(id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.put("/sheep/", response_model=Sheep)
def update_sheep(sheep: Sheep):
    return db.update_sheep(sheep)