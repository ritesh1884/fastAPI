from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allowed origin ( frontend url )
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # means all apis(get, post, put, delete) are allowed
    allow_headers=["*"],   # means all headers are allowed
)


@app.get("/")
def home():
    return {"message": "CORS is enabled for this FastAPI application!"}


# frontend code
# https://youtu.be/wizGGl4APXI?si=v7OmVLjFOdFYYlbb&t=345

