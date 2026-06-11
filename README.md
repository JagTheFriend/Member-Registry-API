# Member Registry API

A standalone Member Registry API Service built with FastAPI.

## Features

- **CRUD operations** for managing members
- **Pydantic models** for request/response validation
- **JSON file persistence** — no database setup required
- **OpenAPI docs** auto-generated at `/docs`

## Endpoints

| Method | Path               | Description          |
| ------ | ------------------ | -------------------- |
| GET    | `/members/`        | List all members     |
| GET    | `/members/{id}`    | Get a member by ID   |
| POST   | `/members/`        | Create a new member  |
| PUT    | `/members/{id}`    | Update a member      |
| DELETE | `/members/{id}`    | Delete a member      |
| GET    | `/health`          | Health check         |

## Member Schema

| Field            | Type    | Required | Description                          |
| ---------------- | ------- | -------- | ------------------------------------ |
| `id`             | string  | auto     | Unique identifier (UUIDv4)           |
| `name`           | string  | yes      | Full name (1-100 chars)              |
| `email`          | string  | yes      | Valid email address                  |
| `phone`          | string  | no       | Phone number (10-15 digits, optional)|
| `membership_date`| date    | yes      | Registration date (ISO 8601)         |
| `active`         | boolean | no       | Whether the member is active         |

## Quick Start

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/)

### Install & Run

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

### Example

```bash
curl -X POST http://localhost:8000/members/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "membership_date": "2025-01-15"
  }'
```
