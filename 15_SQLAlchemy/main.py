from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session 
from fastapi import FastAPI, Depends

app = FastAPI()

DATABASE_URL = 'sqlite:///./test.db' 
engine = create_engine(
    DATABASE_URL,
    connect_ags = {"check_same_thread":False}
)

sessionLocal = sessionmaker(bind = engine)
base = declarative_base()


class Toddo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key= True, index= True)
    title = Column(String)
    completed = Column(String)

base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
            db.close()

@app.get( "/get")
def home(db: Session = Depends(get_db)):
     return {
          "message": "DB Connected."
     }