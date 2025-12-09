from fastapi import FastAPI
import uvicorn

appn = FastAPI()

@appn.get("/")
def read_root():
    return {"Hello": "World"}

@appn.get("/call/start")
def start_call():
    return {
        "call id": "CALL 123",
        "status": "starting..."
    }

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn fast:appn --reload --host 0.0.0.0

https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev
https://glorious-pancake-9g6v5jvj59vhp69v-8000.app.github.dev/call/start
"""