from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "CORS is enabled for this FastAPI application!"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b} 