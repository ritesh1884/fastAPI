from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# /users/101?notify=true
# path params - /users/101
# query - ?notify=true
# req body 
# {
#     "name": "Ritesh"
# }



users = []
class User(BaseModel):
    name: str
    age:int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":" User created successfully",
        "data": user
    }



# updating the data
@app.put("/users/{user_id}")
def updated_user(user_id:int, user:User, notify:bool =False):
    if user_id <len(users):
        users[user_id] = user
        return{
            "message":"User created successfully",
            "notify": notify,
            "data": user
        }
    return{
        "error": "User not found "
    }


# https://youtu.be/femcBliYfl0?si=uwsOwoqEzMl-zPmI&t=431
