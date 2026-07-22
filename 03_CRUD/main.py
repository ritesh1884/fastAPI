from fastapi import FastAPI
from pydantic import BaseModel   # we can validate data and define the data strucutre

app = FastAPI()

# get route
# @app.get("/home")
# def home():
#     return {"message":"Welcome to home page"}

# @app.get("/about")
# def about():
#     return {"message":'This is about page'}

# post route
# @app.post("/create-user")
# def create_user(name:str, age:int):
#     return{
#         "name":name,
#         "age":age
#     }

# test post api onm swagger by using http://127.0.0.1:8000/docs




# @app.post("/create-user")
# def create_user(user:dict):  # pura user ka data deklhna hai so use dictonary
#     return{
#         "message":"User created",
#         "data":user
#     }


# validating data
class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:User): 
    return{
        "message":"User created",
        "data":user
    }