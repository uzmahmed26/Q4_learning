📘 FastAPI Dependency Injection – Mini Project
This project demonstrates Step 4: Dependency Injection in FastAPI with simple, real-world examples. Dependency Injection (DI) allows you to write reusable, testable, and organized code by separating common logic (like login checks, data fetching, or validations) into dedicated functions or classes.

✅ Key Concepts Covered:
Simple Function-Based Dependencies

Dependencies with Query Parameters

Multiple Dependencies in a Route

Class-Based Dependencies for Error Handling

Clean use of Depends() and Annotated

📂 Project Structure
main.py – Contains all example endpoints explained step-by-step.

🚀 How to Run
bash
Copy
Edit
uvicorn main:app --reload
Then visit:
http://127.0.0.1:8000/docs
