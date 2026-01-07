# Fintech Fraud Detection API

## 🚀 Project Overview

This is a **Fraud Detection System** built as a backend application for financial transactions.  
The goal of the project is to **detect fraudulent transactions** in real-time using machine learning and REST APIs.

Users (apps or services) can **send transaction data** to this API, and it returns whether the transaction is **fraudulent or normal**.

---

## 🧠 Key Features

✔ REST API for submitting transaction data  
✔ Real-time prediction using a trained ML model  
✔ Idempotency for safe repeated requests  
✔ Alerts and rule-based checks  
✔ Database support with PostgreSQL/SQLite  
✔ Docker support for containerized deployment  
✔ Well-structured, modular Python backend

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python |
| API Framework | FastAPI |
| Machine Learning | LightGBM / Scikit-learn |
| Database | PostgreSQL / SQLite |
| Caching | Redis |
| ORM | SQLAlchemy |
| Testing | Pytest |
| Containerization | Docker |
| Deployment | Any Cloud or Local |

---


---

## 🧪 How It Works

1. A client sends transaction data to `/predict` endpoint.  
2. The app preprocesses and validates input.  
3. A trained ML model classifies transaction as **fraud** or **normal**.  
4. Result is returned as JSON response.  
5. Optional alerts or rules can be triggered.

---

## 📦 Getting Started

### 🧰 Prerequisites

Install Python 3.10 or above.

---

### 📂 Install Dependencies

```bash
pip install -r requirements.txt

#start the App(Local)
uvicorn app.main:app --reload

#Example API Request

curl -X POST "http://localhost:8000/predict" \
   -H "Content-Type: application/json" \
   -d '{
         "transaction_id": "12345",
         "amount": 5000,
         "customer_id": "C001",
         "features": [...]
       }'

