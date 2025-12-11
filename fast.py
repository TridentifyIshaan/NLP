from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

appn = FastAPI()

@appn.get("/")
def read_root():
    return {"Hello": "World", "Namaste": "दुनिया"}

@appn.get("/call/start")
def start_call():
    return {
        "call id": "CALL 123",
        "status": "starting..."
    }

@appn.get("/hello/{name}")
def greet(name: str):
    return {
        "greeting": f"Hello {name}",
        "length_of_name": len(name)
    }

@appn.get("/info")
def info(age: int, city: str = "Unknown"):
    return {
        "age": age,
        "city": city,
        "adult": age >= 18
    }

@appn.post("/form-items/")
async def create_form_item(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    tax: float = Form(...)
):
    return {
        "name": name,
        "description": description,
        "price": price,
        "tax": tax,
    }

class Item(BaseModel):
    name: str
    descr: str | None = None
    price: float
    tax: float | None = None

@appn.post("/json-items/")
async def create_json_item(item: Item):
    return item

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn fast:appn --reload --host 0.0.0.0

https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/call/start
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/hello/Ishaan
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/info?age=19&city=ghaziabad
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/form-items/
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/json-items/

Ctrl + C to stop the server
"""