from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def welcome():
    return {"message: Welcome User"}

# To run the server: uvicorn main:app --reload
# to install in en environment: uv pip install name