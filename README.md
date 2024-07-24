# fastapi-backend-template
Backend Template in Python using FastAPI, SQLAlchemy, Pydantic and Pytest.

This is an attempt to Apply MVC Concept to FastAPI w/ ORM using SQLAlchemy. With in mind that this code may also be use later on as a template for File Structured Software Architecture Backend using Python.

## Basic File Structure

- main.py - the FastAPI Main Application
- /api - contain all code for Backend FastAPI structure (Controllers, Models, Schemas etc)
- /config - contain configuration setup for database
- /helper - contain additional function or module to handle other task that may be use to /api such as password hashing or token generation.

- /api/v1/controller - contain all controller logic that will define the endPoint and use the Service
- /api/v1/models - conatin all models that utilize the SQLAlchemy
- /api/v1/schemas - contain all schema to validate the input and output of API using Pydantic
- /api/v1/routers - contain all router from controllers for structuring the url path.
- /api/v1/services - contain business logic that utilize the models.

For running, use the command 
```
fastapi dev main.py
```

For Automated Testing, use the command
```
pytest
```
