# from fastapi import FastAPI
# import time, asyncio
# app = FastAPI()


# # sync 
# def task():
#     time.sleep(3)
#     return "Done"


# # async code
# async def task():
#     await asyncio.sleep(3)
#     return "Done"







# using fast api
from fastapi import FastAPI
import time, asyncio
app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"Async API"
    }