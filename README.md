# Web Application Documentation

## Overview

This document outlines the design and implementation of a web application following the MVC design pattern. The application is built using Python and FastAPI, interfacing with a MySQL database using SQLAlchemy for ORM, and employs Pydantic for data validation.

## Directory Structure

```

app
├── **init**.py
├── config.py
├── controllers
│ ├── **init**.py
│ ├── post.py
│ └── user.py
├── db.py
├── dependencies.py
├── main.py
├── models
│ ├── **init**.py
│ ├── post.py
│ └── user.py
├── schemas
│ ├── **init**.py
│ ├── post.py
│ └── user.py
├── services
│ ├── **init**.py
│ └── auth_service.py
└── tests
├── **init**.py
├── test_post.py
└── test_user.py
requirements.txt
.env
pytest.ini
run_tests.sh

```

## Environment Variables

Environment variables are managed using Pydantic's `BaseSettings`. The configuration is stored in `config.py` and loaded from a `.env` file.

```python
# config.py
import os
from pydantic_settings import BaseSettings

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = f"app/configs/{ENVIRONMENT}.env"

settings = Settings()
```

## Authentication

Authentication is handled using JWT tokens. The tokens are generated and verified in `auth_service.py`.

## Request Validation

Payload size validation is implemented in the `dependencies.py` module to ensure that the payload does not exceed 1 MB for the "AddPost" endpoint.

```python
# dependencies.py
from fastapi import Request, HTTPException

async def validate_payload_size(request: Request):
    content_length = request.headers.get('content-length')
    if content_length and int(content_length) > 1024 * 1024:  # 1 MB limit
        raise HTTPException(status_code=413, detail="Payload too large")
```

## Caching

The "GetPosts" endpoint uses in-memory caching with `cachetools` to cache responses for up to 5 minutes for the same user.

## Endpoints

### Signup Endpoint

- **URL**: `/users/signup`
- **Method**: POST
- **Payload**: `{ "email": "email@example.com", "password": "password" }`
- **Response**: JWT token upon successful registration.

### Login Endpoint

- **URL**: `/users/login`
- **Method**: POST
- **Payload**: `{ "email": "email@example.com", "password": "password" }`
- **Response**: JWT token upon successful login.

### AddPost Endpoint

- **URL**: `/posts/`
- **Method**: POST
- **Payload**: `{ "text": "Hello, World!" }`
- **Headers**: `{ "Authorization": "Bearer <token>" }`
- **Response**: `postID` upon successful post creation.
- **Validation**: Ensures payload does not exceed 1 MB.

### GetPosts Endpoint

- **URL**: `/posts/`
- **Method**: GET
- **Headers**: `{ "Authorization": "Bearer <token>" }`
- **Response**: List of user's posts.
- **Caching**: Responses cached for up to 5 minutes for the same user.

### DeletePost Endpoint

- **URL**: `/posts/{post_id}`
- **Method**: DELETE
- **Headers**: `{ "Authorization": "Bearer <token>" }`
- **Response**: Confirmation of post deletion

.

## Running the Application

1. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

2. **Run Database Migrations**:

   ```sh
   python -c 'from app.db import Base, engine; Base.metadata.create_all(bind=engine)'
   ```

3. **Start the Application**:

   ```sh
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Run Tests**:
   ```sh
   pytest
   ```

## Conclusion

This application is designed to be modular and follows best practices in web application development. The use of environment variables, request validation, and caching ensures it is secure, efficient, and scalable.

````

### Final Steps

1. **Ensure All Tests Pass**:
   ```sh
   pytest
````

2. **Commit and Push to GitHub**:

   ```sh
   git add .
   git commit -m "Completed web application with all requirements"
   git push origin main
   ```

3. **Submit Your Repository Link**:
   Email the repository link to `lucidtasksubmission@gmail.com`.

By following these steps, you ensure your application meets all the specified requirements and is ready for submission.
