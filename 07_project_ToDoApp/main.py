from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed: bool

# creating the api
@app.post("/create-todo")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message": "Task created",
        "data": todo
    }

# getting all the data
@app.get("/todos")
def get_todos():
    return todos









# get a single data based on idd
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "No task found"} # if no task found






# updating the data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, update_todo:Todo): # we will replace todo_id with update_todo
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {
                "message": "Updated",
                "data": update_todo
            }
    return {"error": "No task found"}






# deleting the task
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
     for index, todo in enumerate(todos):
            if todo.id == todo_id:
                todos.pop(index)
                return{
                    "message": "Task deleted successfully"
                }
     return {"error": "No task found"}
    
