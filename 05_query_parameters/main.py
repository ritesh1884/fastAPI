# path parameter means dynamic routes
from fastapi import FastAPI

app = FastAPI()

# query parameters = users?name=ritesh


# defining datatype of 
# @app.get("/users")
# def get_user(name):  # ye name query params se utha rhe hai
#     return {"Name": name}

# http://127.0.0.1:8000/users?name=ritesh => {"Name":"ritesh"}

# It will also give an error {"detail":[{"type":"missing","loc":["query","name"],"msg":"Field required","input":null}]}
# which we can handle it using optional parameters


# @app.get("/users")
# def get_user(name: str = None):  # just give str as none means agar name na mile then show null
#     return {"Name": name}

# http://127.0.0.1:8000/users => {"Name":null}




# setting a default value
# @app.get("/products")
# def get_user(limit: int = 10):  
#     return {"limit": limit}

# http://127.0.0.1:8000/products => {"limit":10}
# http://127.0.0.1:8000/products?limit=300   => {"limit":300}





# handling multiple query params
@app.get("/items")
def get_user(name: str = None , price: int = 0):  
    return { 
        "name": name, "price": price 
    }

# http://127.0.0.1:8000/items => {"name":null,"price":0}
# http://127.0.0.1:8000/items?name=laptop&price=66000 => {"name":"laptop","price":66000}