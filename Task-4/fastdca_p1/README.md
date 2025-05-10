📝 Project Summary – FastAPI Item Management API
Project Name: 🚀 FastAPI Item Management API
🔍 Overview
This is a beginner-friendly API project built using FastAPI. It demonstrates how to use different types of parameters such as:

✅ Path Parameters

✅ Query Parameters

✅ Request Body (JSON)

✅ Headers

🎯 Purpose
The goal of this project is to:

Show how to create structured and validated APIs using FastAPI.

Help beginners learn how FastAPI handles input validation.

Provide hands-on examples for testing with Swagger and ReDoc.

📦 Features
Feature	Description
/users/{user_id}	Gets user info by Path parameter with validation
/courses/	Filters course list using Query parameters like topic, skip, limit
/items/validated/{item_id}	Updates item using Path, Query, and Body data
/items/{item_id} with X-Custom-Header	Demonstrates how to receive Header values

## 📦 Features

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage with a welcome message |
| `/users/{user_id}` | GET | Uses Path Parameters with validation |
| `/courses/` | GET | Uses Query Parameters: topic, skip, limit |
| `/items/validated/{item_id}` | PUT | Combines Path, Query, and Body parameters |
| `/items/{item_id}` | GET | Uses Path and custom Header parameter (`X-Custom-Header`) |

---

## 📥 Input Types Demonstrated

- **Path Parameters**: `/users/{user_id}`
- **Query Parameters**: `/courses?topic=Python&limit=5`
- **Request Body**: JSON data with item info
- **Headers**: `X-Custom-Header` in `/items/{item_id}`


🔧 How to Run the Project
# 1. Install dependencies
pip install fastapi uvicorn pydantic
# 2. Run the server
uvicorn main:app --reload


