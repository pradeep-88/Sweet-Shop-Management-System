# 🍬 Sweet Shop Management System – Backend API

> **A secure, scalable backend API for managing sweets, users, and sales**  
> Built with modern backend technologies and real-world architecture practices.

---

## 🚀 Project Overview

The **Sweet Shop Management System – Backend** is a RESTful API that powers a sweet shop application.  
It supports secure authentication, role-based access control, inventory management, and sales tracking.

This backend is designed to be consumed by a modern frontend SPA (React / Vue / Angular).

---

## ✨ Key Features

🔐 JWT Authentication & Authorization  
👥 Role-Based Access Control (Admin / User)  
🍭 Sweet Inventory Management (CRUD)  
🛒 Purchase & Sales Management  
📦 PostgreSQL Database Integration  
⚡ High-performance FastAPI backend  
🧱 Clean Architecture (Routes → Services → Repositories)

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python 3.13 🐍 |
| Framework | FastAPI ⚡ |
| Database | PostgreSQL 🐘 |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Authentication | JWT (OAuth2 Password Flow) |
| Password Hashing | bcrypt (Passlib) |
| ASGI Server | Uvicorn |

---

## 📁 Backend Folder Structure

```
backend/
├── alembic/                # Database migrations
├── app/
│   ├── api/
│   │   ├── routes/          # API routes (auth, sweets, sales)
│   │   └── deps.py          # JWT & auth dependencies
│   ├── core/                # Security & configuration
│   ├── database/            # DB session & imports
│   ├── models/              # SQLAlchemy models
│   ├── repositories/        # Database access layer
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   └── main.py              # FastAPI app entry
├── alembic.ini
├── requirements.txt
└── .env
```

---

## 🔑 Authentication Flow

1️⃣ **Register User**  
```
POST /auth/register
```

2️⃣ **Login**  
```
POST /auth/login
```

3️⃣ **Authorized Requests**  
```
Authorization: Bearer <access_token>
```

---

## 🧑‍💼 Role-Based Access

| Role | Permissions |
|----|------------|
| **Admin** 👑 | Add, update, delete sweets |
| **User** 🙋 | View sweets, purchase sweets |

Authorization is enforced using FastAPI dependencies and JWT claims.

---

## 🍭 Core API Endpoints

### 🔐 Auth
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### 🍬 Sweets
- `GET /sweets`
- `POST /sweets` *(Admin only)*
- `PUT /sweets/{id}` *(Admin only)*
- `DELETE /sweets/{id}` *(Admin only)*

### 🛒 Sales
- `POST /sales`
- `GET /sales`

---

## 🗄️ Database & Migrations

PostgreSQL is used as the primary database.  
Alembic manages schema migrations.

Run migrations:
```bash
alembic upgrade head
```

---

## ▶️ Running the Backend Locally

Activate virtual environment:
```bash
source .venv/bin/activate
```

Start server:
```bash
uvicorn app.main:app --reload
```

Open API documentation:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Testing

- Swagger UI → `/docs`
- OpenAPI Spec → `/openapi.json`

---

## 🎯 Assignment Coverage

✔ RESTful API design  
✔ Secure authentication & authorization  
✔ Database integration  
✔ Clean architecture  
✔ Scalable backend implementation  

This backend fully satisfies the **server-side requirements** of the assignment.

---

## 🤝 Contributors

👨‍💻 **Primary Author:** Pradeep Sw  
🤖 **Co-Author:** ChatGPT (AI Assistant)

---

## 📌 Next Phase

🖥️ Frontend (React SPA)  
📊 Admin dashboard  
🔍 Search & filtering  
🎨 UI/UX enhancements  

---

✨ *Built with clarity, scalability, and real-world backend practices in mind.*
