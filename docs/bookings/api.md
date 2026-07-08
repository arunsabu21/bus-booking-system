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

## Create Booking

**Endpoint**

```http
POST /api/v1/bookings/create/
```

**Authentication**

Required

**Headers**

```text
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body**

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_count": 2
}
```

**Response**

```text
Status: 201 Created
```

```json
{
  "id": "fe47e271-e9b7-473c-b64e-ef1d7494f3eb",
  "booking_reference": "BK-1011B2BF",
  "user": "user@gmail.com",
  "trip": "Chennai → Bengaluru",
  "seat_count": 2,
  "total_amount": "1700.00",
  "status": "CONFIRMED",
  "created_at": "2026-07-08T11:53:42.765421+05:30",
  "updated_at": "2026-07-08T11:53:42.765443+05:30"
}
```




