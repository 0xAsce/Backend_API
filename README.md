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

- Python 3.10+
- Django 6.0+
- Django REST Framework

Install dependencies:

```bash
pip install -r requirements.txt
