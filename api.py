from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from model import Chat

app = FastAPI()

# Mock database to store data
db = {}

# Model for your data
class Item(BaseModel):
    data: list[dict] = None


# POST endpoint to create a new item
@app.post("/items/")
async def create_item(id: int, prompt: str):
    try:
        if id not in db:
            db[id] = []
            data = None
        else:
            data = db[id]

        generated_text = Chat(data, prompt) # data is a list of dicts like {"role": "USER/CHATBOT", "message": "..."}

        db[id].append({"role": "USER", "message": prompt})
        db[id].append({"role": "CHATBOT", "message": generated_text})
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET endpoint to retrieve an item by id
@app.get("/items/{id}")
async def read_item(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": db[id]}


# DELETE endpoint to delete an item by id
@app.delete("/items/{id}")
async def delete_item(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[id]
    return {"message": "Item deleted successfully"}


# GET endpoint to retrieve all items
@app.get("/items/")
async def read_all_items():
    return db
