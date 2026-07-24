from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

# sending http code
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create():
    return {
        "message": "User created"
    }

# sending custom response
@app.get("/user")
def get_user():
    return{
        "status": "success",
        "message": "User fetched",
        "data":{
            "name": "Ritesh",
            "age": 22
        }
    }


# output: custom response = "status": "success",
# {
#   "status": "success",
#   "message": "User fetched",
#   "data": {
#     "name": "Ritesh",
#     "age": 22
#   }
# }





# Error handling

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    # if id is correct
    return{
        "id": 1,
        "name": "Ritesh",
            
    }