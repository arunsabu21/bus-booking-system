# Bus Booking System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-REST%20API-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-Cache-DC382D?logo=redis)
![JWT](https://img.shields.io/badge/JWT-SimpleJWT-black)
</p>

## Overview

A scalable and production-ready Bus Booking REST API built with Django, Django REST Framework, PostgreSQL, Redis, and JWT Authentication.

The project follows a clean architecture by separating business logic into Services, Serializers, and Views for maintainability, scalability, and testability.

---

## Features

### Authentication

- User Registration
- Email OTP Verification
- JWT Authentication
- Login
- Logout (Token Blacklisting)
- Forgot Password
- Password Reset
- Login Attempt Rate Limiting
- Redis-based OTP Storage

### Bus Management

- Cities
- Operators
- Routes
- Buses
- Trips
- Trip Search

### Booking System

- Seat Availability
- Seat Selection
- Booking Creation
- Booking Cancellation
- Booking History
- Booking Reference Generation
- Seat Validation

### Performance

- Redis Trip Search Caching
- Optimized Database Queries
- Service Layer Architecture

### Security

- Custom User Model
- Password Hashing
- Django Password Validators
- Environment Variables
- JWT Access & Refresh Tokens
- Redis Cache

---

## Tech Stack

| Category       | Technology            |
| -------------- | --------------------- |
| Language       | Python                |
| Framework      | Django                |
| API            | Django REST Framework |
| Database       | PostgreSQL            |
| Cache          | Redis                 |
| Authentication | SimpleJWT             |

---

## Architecture

```text
Client
   │
Views
   │
Services
   │
Models
   │
PostgreSQL
```

---

## Project Structure

```text
src/
├── authentication/
├── bookings/
├── buses/
├── cities/
├── operators/
├── routes/
├── trips/
├── core/
│   ├── cache/
│   ├── constants/
│   └── settings.py
└── manage.py
```

---

## Authentication Flow

```text
Register
    │
Generate OTP
    │
Store OTP (Redis)
    │
Verify OTP
    │
Activate Account
    │
Login
    │
JWT Authentication
    │
Protected APIs
```

---

## Booking Flow

```text
Search Trip
    │
View Seats
    │
Select Seats
    │
Create Booking
    │
Reserve Seats
    │
Cancel Booking
    │
Release Seats
```

---

## API Documentation

Project documentation is available in the `docs/` directory.

- Authentication
- Cities
- Operators
- Routes
- Buses
- Trips
- Bookings

Each module includes API documentation and testing guides.

---

## Environment Variables

```env
SECRET_KEY=

DEBUG=True

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

REDIS_URL=

LOGIN_ATTEMPT_LIMIT=5
LOGIN_ATTEMPT_TIMEOUT=300

OTP_TIMEOUT=300

FORGOT_TOKEN_TIMEOUT=900
```

---

## Installation

```bash
git clone <repository-url>

cd bus-booking-api

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Testing

- Bruno
- Postman
- Insomnia
- cURL
- Thunder Client 

---

## Roadmap

- Payment Integration
- Ticket Generation
- Notifications
- Pagination
- Filtering
- Docker
- CI/CD
- AWS Deployment

---

## Author

**Arun**

Backend Software Engineer

---

