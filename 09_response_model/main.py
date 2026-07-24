from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# It means sending only relevant details to client/user
class User(BaseModel):
    name:str
    age:int
    password: str

class UserResponse(BaseModel):
    name:str
    age:int  # so now password will not go

@app.get("/user", response_model=UserResponse)
def user():
    return{
        "name":"Ritesh",
        "age": 22,
        "password": "123"
    }