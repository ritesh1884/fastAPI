from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session 
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = 'sqlite:///./test.db' 
engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread":False}
)

sessionLocal = sessionmaker(bind = engine)
base = declarative_base()


class Todo(base):
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

# CREATE api
@app.post( "/todos")
def create_todo(title:str, db: Session = Depends(get_db)):
     todo = Todo(title = title, completed = "False")
     db.add(todo)
     db.commit()
     db.refresh(todo)
     return{
          "message": "todo created",
          "data": todo
     }


# read api
@app.get("/read")
def read(db:Session = Depends(get_db)):
     todos = db.query(Todo).all()
     return{
          "Total":len(todos),
          "data": todos 
     }


# reading data based on id
@app.get("/read/{todo_id}")
def read(todo_id=int, db:Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
          raise HTTPException(status_code=404, detail="Todo not found")
     return todo 


# updating the data
@app.put("/update/{todo_id}")
def update(todo_id:int, title:str,db:Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

     todo.title = title
     db.commit()

     return{
               "message": "todo updated",
               "data": todo
          }


# deleting the data
@app.delete("/delete/{todo_id}")
def delete(todo_id:int,db:Session = Depends(get_db) ):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()
     
     if not todo:
          raise HTTPException(status_code=404, detail="Todo not found")
     
     db.delete(todo)
     db.commit()

     return {
          "message": "Todo deleted"
     }