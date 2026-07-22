# path parameter means dynamic routes
from fastapi import FastAPI

app = FastAPI()

# @app.get("/users/{user_id}")
# def get_user(user_id):
#     return {"user_id": user_id}


# defining datatype of 
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id": user_id}
# http://127.0.0.1:8000/users/dfgr:
# {"detail":[{"type":"int_parsing","loc":["path","user_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"dfgr"}]}

