from fastapi import FastAPI, Depends, HTTPException, Query, status
from typing import Annotated

app = FastAPI()

# ✅ Example 1: Simple Dependency
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response

# ✅ Example 2: Dependency with parameters
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response

# ✅ Example 3: Query Parameters (Login Simulation)
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    return {"message": "Login Failed"}

@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user

# ✅ Example 4: Multiple Dependencies
def depfunc1(num: int):
    return num + 1

def depfunc2(num: int):
    return num + 2

@app.get("/main/{num}")
def get_main(
    num: int,
    num1: Annotated[int, Depends(depfunc1)],
    num2: Annotated[int, Depends(depfunc2)]
):
    total = num + num1 + num2
    return {"result": f"Pakistan {total}"}

# ✅ Example 5: Class-Based Dependency (404 simulation)
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return {"blog": blog_name}

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return {"user": user_name}
