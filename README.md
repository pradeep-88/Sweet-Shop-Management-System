# 🍬 Sweet Shop Management System – Backend API

> **A secure, scalable backend API for managing sweets, users, and sales**  
> Built using modern backend technologies and real-world architecture practices.

---

## 🚀 Project Overview

The **Sweet Shop Management System – Backend** is a RESTful API that powers a sweet shop application.  
It provides secure authentication, role-based access, inventory management, and sales handling.

This backend is designed to be consumed by a modern frontend SPA (React / Vue / Angular).

---

## ✨ Key Features

🔐 JWT Authentication & Authorization  
👥 Role-Based Access Control (Admin / User)  
🍭 Sweet Inventory Management (CRUD)  
🛒 Purchase & Sales Management  
📦 PostgreSQL Database Integration  
⚡ FastAPI High-Performance API  
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
| Auth | JWT (OAuth2 Password Flow) |
| Password Hashing | bcrypt (Passlib) |
| Server | Uvicorn |

---

## 📁 Backend Folder Structure

backend/
├── alembic/ # Database migrations
├── app/
│ ├── api/
│ │ ├── routes/ # API routes (auth, sweets, sales)
│ │ └── deps.py # JWT & auth dependencies
│ ├── core/ # Security & config
│ ├── database/ # DB session & imports
│ ├── models/ # SQLAlchemy models
│ ├── repositories/ # Database access layer
│ ├── schemas/ # Pydantic schemas
│ ├── services/ # Business logic
│ └── main.py # FastAPI app entry
├── alembic.ini
├── requirements.txt
└── .env


---

## 🔑 Authentication Flow

1️⃣ Register User  

2️⃣ Login  

3️⃣ Use JWT Token  

---

## 🧑‍💼 Role-Based Access

| Role | Permissions |
|----|------------|
| Admin 👑 | Add, update, delete sweets |
| User 🙋 | View sweets, purchase sweets |

Authorization is enforced using FastAPI dependencies and JWT claims.

---

## 🍭 API Endpoints

### 🔐 Auth
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

### 🍬 Sweets
- GET `/sweets`
- POST `/sweets` (Admin only)
- PUT `/sweets/{id}` (Admin only)
- DELETE `/sweets/{id}` (Admin only)

### 🛒 Sales
- POST `/sales`
- GET `/sales`

---

## 🗄️ Database & Migrations

PostgreSQL is used as the primary database.  
Alembic handles schema migrations.

Run migrations:
```bash
alembic upgrade head

---

## 🧑‍💼 Role-Based Access

| Role | Permissions |
|----|------------|
| Admin 👑 | Add, update, delete sweets |
| User 🙋 | View sweets, purchase sweets |

Authorization is enforced using FastAPI dependencies and JWT claims.

---

## 🍭 API Endpoints

### 🔐 Auth
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

### 🍬 Sweets
- GET `/sweets`
- POST `/sweets` (Admin only)
- PUT `/sweets/{id}` (Admin only)
- DELETE `/sweets/{id}` (Admin only)

### 🛒 Sales
- POST `/sales`
- GET `/sales`

---

## 🗄️ Database & Migrations

PostgreSQL is used as the primary database.  
Alembic handles schema migrations.

Run migrations:
```bash
alembic upgrade head
source .venv/bin/activate

uvicorn app.main:app --reload
http://127.0.0.1:8000/docs



  
