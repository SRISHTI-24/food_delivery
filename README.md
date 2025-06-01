# Food Delivery Backend

This project is a backend system for a food delivery application built using **FastAPI**, **PostgreSQL**, and a **microservices architecture**.

## 🧩 Microservices Overview

The system is divided into three microservices:

1. **User Service** – Handles:
   - Fetching available restaurants
   - Placing orders
   - Submitting ratings

2. **Restaurant Service** – Handles:
   - Restaurant & menu management
   - Accepting/rejecting orders
   - Assigning delivery agents

3. **Delivery Agent Service** – Handles:
   - Managing delivery agent availability
   - Updating order delivery status

## 🛠️ Technologies Used

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Uvicorn**
- **Docker** *(optional for deployment)*

## 🚀 Running the Services

Each microservice runs independently. Example for running a FastAPI service:

```bash
user_service (8001)  # or resturant_service (8000) / delivery_service (8002)
python -m uvicorn <any_service>.main:app --reload --port <port_no> # Change port per service
e.g., for User_service
"python -m uvicorn user_service.main:app --reload --port 8001"
