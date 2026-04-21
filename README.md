# Notes API

A simple CRUD API built with FastAPI.

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /notes | Create a note |
| GET | /notes | Get all notes |
| GET | /notes/{id} | Get note by id |
| PUT | /notes/{id} | Update a note |
| DELETE | /notes/{id} | Delete a note |

## Setup
pip install fastapi uvicorn
uvicorn main:app --reload
