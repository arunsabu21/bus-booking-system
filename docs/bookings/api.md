# Bookings API

## Overview

The Bookings API allows authenticated users to view their own bookings.

---

## Authentication

All Endpoints require JWT Authentication.

**Authorization Header:**

```
Authorization: Bearer <access_token>
```

---

## Get all bookings

**Base URL**

```
api/v1/bookings/
```

### Description

Returns all booking belonging to the authenticated user.

**Endpoint**

```http
GET /api/v1/bookings/
```

**Authentication**

Required

**Permission**

Authenticated users only.

**Success Response (200 OK)**

```json
[
  {
    "id": "afb45322-bc49-4cf2-8834-d4b3570a4959",
    "booking_reference": "BK000001",
    "user": "user@gmail.com",
    "trip": "Chennai → Bengaluru",
    "seat_count": 2,
    "total_amount": "1700.00",
    "status": "CONFIRMED"
  }
]
```

---

## Get Bookings by ID

**Description**

Returns detailed information for a single booking owned by the authentication user.

**Endpoint**

```http
GET /api/v1/bookings/{booking_id}/
```

**Authentication**

Required

**Permission**

Authenticated users only.

**Success Response (200 OK)**

```json
{
  "id": "afb45322-bc49-4cf2-8834-d4b3570a4959",
  "booking_reference": "BK000001",
  "user": "user@gmail.com",
  "trip": "Chennai → Bengaluru",
  "seat_count": 2,
  "total_amount": "1700.00",
  "status": "CONFIRMED",
  "created_at": "2026-07-07T16:00:13.117645+05:30",
  "updated_at": "2026-07-07T16:00:13.117679+05:30"
}
```

---

## Possible Errors

**Authentication Required**

```
401 Unauthorized
```

**Booking Not Found**

```
404 Not Found
```

**Example:**

```json
{
    "detail": "Booking not found."
}
```




