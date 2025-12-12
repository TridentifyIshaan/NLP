from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# load_dotenv()
load_dotenv()  # load .env values when present

MONGO_URI = os.getenv(
  "MONGO_URI",
  "mongodb+srv://ishaanrastogi19_db_user:8z5P8uLN7JgB3yZc@cluster0.as31dzd.mongodb.net/",
)
DB_NAME = os.getenv("DB_NAME", "test")  # MongoDB database names cannot contain dots, so default to "test"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server running"}

@app.post("/add_user")
async def add_user(user: dict):
    result = await db.users.insert_one(user)
    return {"inserted_id": str(result.inserted_id)}

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn mongo:app --reload --log-level debug
Ctrl + C to stop the server

Testing endpoints with curl:

curl -X POST http://localhost:8000/add_user \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'

"""