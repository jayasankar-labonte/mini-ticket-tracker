# Mini Ticket Tracker

Mini Ticket Tracker is a simple ticket management system built using **FastAPI, PostgreSQL, React, and Redux**.  
It allows users to create, view, update, and manage tickets with pagination and status tracking.

---

## Features

- Create new tickets
- View ticket details
- Edit tickets
- Delete tickets
- Status tracking (NEW, IN_PROGRESS, DONE)
- Pagination
- Status filtering
- Badge-based status indicators
- API testing with pytest

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest

### Frontend
- React
- Redux Toolkit
- Bootstrap
- Axios

---

## Project Structure


mini_ticket_tracker
│
├── backend
│ ├── app
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── schemas.py
│ │ └── models
│ │
│ ├── tests
│ │ └── test_tickets.py
│ │
│ └── requirements.txt
│
├── frontend
│ ├── src
│ │ ├── components
│ │ ├── features
│ │ └── app
│ │
│ └── package.json
│
└── README.md


---

## Backend Setup

### Create Virtual Environment


python -m venv venv


Activate (Windows):


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

### Configure Environment

Create `.env` file inside backend:


DATABASE_URL=postgresql://postgres:password@localhost:5432/mini_ticket_tracker


---

### Run FastAPI


uvicorn app.main:app --reload


API:


http://127.0.0.1:8000


Swagger docs:


http://127.0.0.1:8000/docs


---

## Frontend Setup

Go to frontend folder:


cd frontend


Install dependencies:


npm install


Run React app:


npm start


Frontend runs at:


http://localhost:3000


---

## Running Tests

Run pytest:


pytest


Example output:


4 passed in 1.9s


---

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| POST | /tickets | Create ticket |
| GET | /tickets | List tickets |
| GET | /tickets/{id} | Get ticket |
| PATCH | /tickets/{id} | Update ticket |
| DELETE | /tickets/{id} | Delete ticket |

---

## Author

Jayasankar KR