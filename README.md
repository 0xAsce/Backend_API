# Django ToDo REST API

A simple RESTful API built with **Django** and **Django REST Framework (DRF)** for managing ToDo items. This project allows users to create, read, update, and delete tasks with full authentication and API documentation.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Pagination & Filtering](#pagination--filtering)
- [Authentication](#authentication)
- [Input Validation](#input-validation)
- [Notes](#notes)
- [License](#license)

---

## Features

- User registration and authentication(JWT)
- CRUD operations for ToDo items
- Input validation for all fields
- Pagination and filtering support
- Easy setup and development server
- Works with SQLite by default (can be configured for other DBs)

Each ToDo item includes:

- `id` (auto-generated)
- `title` (string)
- `description` (string)
- `isCompleted` (boolean)
- `createdAt` (timestamp)

---

## Requirements

 Python 3.10+
- Django 6.0+
- Django REST Framework



### Installation

1 - Clone the repository:

- git clone https://github.com/0xAsce/Backend_API.git
- cd Backend_API

2 - Create a virtual environment (optional but recommended):

- python -m venv venv
- source venv/bin/activate  # Linux/Mac
- venv\Scripts\activate     # Windows

3 - Install dependencies:

- pip install -r requirements.txt

4 - Apply migrations to create the database:

- python manage.py migrate

5 - Create a superuser for admin access:

- python manage.py createsuperuser

6 - Run the development server:

- python manage.py runserver

- Access the API at http://127.0.0.1:8000/



### API Endpoints
## Method	Endpoint	Description
# POST	/api/register/	Register a new user
# POST	/api/login/	Obtain auth token
# GET	/api/todos/	List all ToDos
# POST	/api/todos/	Create a new ToDo
# GET	/api/todos/{id}/	Get ToDo details
# PUT	/api/todos/{id}/	Update a ToDo
# DELETE	/api/todos/{id}/	Delete a ToDo
