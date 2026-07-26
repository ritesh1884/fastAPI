from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id!=1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )
#     return{
#         "id":1,
#         "name":"Ritesh"
#     }




# custom exceptiom

# class UserNotFoundException(Exception):
#     def __init__(self, name:str):
#         self.name = name

# @app.get("/user/{name}")
# def get_user(name:str):
#     if name!="Ritesh":
#         raise UserNotFoundException(name)
#     return{
#         "name":name
#     }






# Therre is an issue. Internal Server Error will occur if the nameis wrong 
# so we are using global exception handling


class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found(request: Request, exe: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exe.name} not found"
        }
    )
    
@app.get("/user/{name}")
def get_user(name:str):
    if name!="Ritesh":
        raise UserNotFoundException(name)
    return{
        "name":name
    }



