from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import List, Optional
from datetime import date

app = FastAPI()

# ========== Pydantic Models ==========

class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=20)

class UserRead(UserCreate):
    id: int

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: int

    @validator("due_date")
    def due_date_not_past(cls, v):
        if v < date.today():
            raise ValueError("due_date must be today or in the future")
        return v

    @validator("status")
    def valid_status(cls, v):
        if v not in {"pending", "in_progress", "completed"}:
            raise ValueError("Status must be 'pending', 'in_progress', or 'completed'")
        return v

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int

    @validator("due_date")
    def due_date_not_past(cls, v):
        if v < date.today():
            raise ValueError("due_date must be today or in the future")
        return v

class TaskUpdate(BaseModel):
    status: str

    @validator("status")
    def valid_status(cls, v):
        if v not in {"pending", "in_progress", "completed"}:
            raise ValueError("Status must be 'pending', 'in_progress', or 'completed'")
        return v

# ========== In-Memory Storage ==========
USERS: dict[int, UserRead] = {}
TASKS: dict[int, Task] = {}
user_id_counter = 1
task_id_counter = 1

# ========== User Endpoints ==========

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    new_user = UserRead(id=user_id_counter, **user.dict())
    USERS[user_id_counter] = new_user
    user_id_counter += 1
    return new_user

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]

# ========== Task Endpoints ==========

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    new_task = Task(
        id=task_id_counter,
        status="pending",  # default status
        **task.dict()
    )
    TASKS[task_id_counter] = new_task
    task_id_counter += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, update: TaskUpdate):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    task = TASKS[task_id]
    task.status = update.status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task.user_id == user_id]

@app.get("/")
def root():
    return {"message": "Task Tracker API is running!"}
