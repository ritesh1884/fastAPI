from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "my-secret"
ALGORITHM = "HS256"

# creating a token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


# login api 
@app.post("/login")
def login(username: str, password: str):
    if username != "john" or password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": username}) 

    return {"access_token": token}


# verify token
def verify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


# protected route
@app.get("/protected")
def protected_route(user = Depends(verify_token)):
    return {
        "message": f"Hello {user}, you have access to this protected route!",
        "user": user
    }