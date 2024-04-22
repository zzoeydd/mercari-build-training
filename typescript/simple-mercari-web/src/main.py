import uvicorn
from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import hashlib
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

os.makedirs("images", exist_ok=True)

app.mount("/static", StaticFiles(directory="images"), name="static")

class Item(BaseModel):
    name: str
    category: str

# Try to load items from JSON file, if exists
try:
    with open("items.json", "r") as f:
        items = json.load(f)["items"]
except FileNotFoundError:
    items = []

origins = [os.environ.get("FRONT_URL", "http://localhost:3000")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Save items back to the JSON file
def save_items():
    with open("items.json", "w") as f:
        json.dump({"items": items}, f)

@app.get("/")
def root():
    return {"message": "Hello, world!"}

@app.post("/items")
async def add_item(name: str = Form(...), category: str = Form(...), image: UploadFile = File(...)):

@app.get("/items/{item_id}")
def get_item(item_id: int):


@app.get("/image/{item_id}.jpg")
def serve_image(item_id: int):

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
