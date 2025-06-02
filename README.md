
# 🍔 Food Delivery System

A modular **Food Delivery Backend** project built using Python and FastAPI. The system is broken into three independent microservices:

- 🧍 `user_service`
- 🍽️ `resturant_service`
- 🚚 `delivery_agent_service`

Each service handles its own responsibilities and communicates with others over HTTP.

---

## 📁 Project Structure

```
food_delivery/
├── delivery_agent_service/
├── frontend/
├── resturant_service/
├── user_service/
├── requirement.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/srishti24/food_delivery.git
cd food_delivery
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Unix/Mac
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Run Each Microservice

Go to each service directory and start the FastAPI server:

```bash
# Example for user_service
cd user_service
python -m user_service.main:app --reload --port 8001
```

> 💡 Make sure each service runs on a **different port** (e.g., 8000, 8001, 8002)
# user_service: 8001
# resturant_service: 8000
# delivery_agent_service: 8002
---

## 🚀 API Endpoints

### 📦 `user_service`

| Method | Endpoint              | Description                           |
|--------|-----------------------|---------------------------------------|
| GET    |`/resturants/available`| Get list of available restaurants     |
| POST   | `/orders`             | Place a new order                     |
| POST   | `/ratings`            | Submit restaurant/order rating        |

---

### 🍽️ `resturant_service`

| Method | Endpoint                        | Description                                 |
|--------|----------------------------------|--------------------------------------------|
| POST   | `/menu`                          | Create menu items.           |
| GET    | `/menu/{resturant_id}`           | Display menu of particular resturant       |
| POST   | `/menu/{resturant_id}/{item_id}` | Update menu                                |
| POST   | `/menu/{resturant_id}/{item_id}` | Delete item                                |
| GET    | `/orders/pending`                | View pending orders                        |
| POST   | `/orders/{order_id}/accept`      | Accept an order & autoassign deliver agent |
| POST   | `/orders/{order_id}/reject`      | Reject an order                            |

---

### 🚚 `delivery_agent_service`

| Method | Endpoint                            | Description                          |
|--------|-------------------------------------|--------------------------------------|
| GET    | `/available-agents`                 | List available delivery agents       |
| PUT    | `/update-status`                    | Update delivery status               |


## 🧾 License

This project is open source and available under the [MIT License](LICENSE).
