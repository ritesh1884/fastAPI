from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Ensure upload folder exists
UPLOAD_DIR = "uploads" 

# If folder is not created, create it
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# static file setup
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


# upload file api
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "fileName": filename, 
            "message": "File uploaded successfully",
            "file_url": f"http://localhost:8000/files/{filename}"
            }


# get file url
@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return {
        "fileName": filename,
        "file_url": f"http://localhost:8000/uploads/{filename}"
    }


# testing the api
@app.get("/")
def home():
    return {"message": "Welcome to the File Upload API!"}