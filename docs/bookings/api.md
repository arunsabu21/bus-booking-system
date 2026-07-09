# Bookings API

## Overview

The Bookings API allows authenticated users to create, view and manage their own bookings.

---

## Authentication

All endpoints require JWT Authentication.

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

---

# Get All Bookings

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
    "id": "6b9b8993-6d2a-4f8e-ada4-f7f50e4cbeef",
    "booking_reference": "BK-09D9F732",
    "user": "user@gmail.com",
    "trip": "Chennai → Bengaluru",
    "seat_count": 2,
    "seat_numbers": [
      "S1",
      "S2"
    ],
    "total_amount": "1700.00",
    "status": "CONFIRMED"
  }
]
```

---

# Get Booking Details

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
  "id": "6b9b8993-6d2a-4f8e-ada4-f7f50e4cbeef",
  "booking_reference": "BK-09D9F732",
  "user": "user@gmail.com",
  "trip": "Chennai → Bengaluru",
  "seat_count": 2,
  "seat_numbers": [
    "S1",
    "S2"
  ],
  "total_amount": "1700.00",
  "status": "CONFIRMED",
  "created_at": "2026-07-09T15:57:00.633702+05:30",
  "updated_at": "2026-07-09T15:57:00.633736+05:30"
}
```

---

# Create Booking

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

### Request Body

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_numbers": [
    "S1",
    "S2"
  ]
}
```

### Success Response (201 Created)

```json
{
  "id": "6b9b8993-6d2a-4f8e-ada4-f7f50e4cbeef",
  "booking_reference": "BK-09D9F732",
  "user": "user@gmail.com",
  "trip": "Chennai → Bengaluru",
  "seat_count": 2,
  "seat_numbers": [
    "S1",
    "S2"
  ],
  "total_amount": "1700.00",
  "status": "CONFIRMED",
  "created_at": "2026-07-09T15:57:00.633702+05:30",
  "updated_at": "2026-07-09T15:57:00.633736+05:30"
}
```

### Validation Rules

- At least one seat must be selected.
- Duplicate seat numbers are not allowed.
- Already booked seats cannot be booked again.
- Selected seats must belong to the trip.
- Seat numbers are case-insensitive.

---

# Cancel Booking

**Endpoint**

```http
PATCH /api/v1/bookings/{booking_id}/cancel/
```

**Authentication**

Required

**Permission**

Authenticated users only.

**Request Body**

None

**Success Response (200 OK)**

```json
{
  "message": "Booking cancelled successfully."
}
```

---

# Possible Errors

## Authentication Required

```text
401 Unauthorized
```

---

## Booking Not Found

```text
404 Not Found
```

```json
{
  "detail": "Booking not found."
}
```

---

## Seat Already Booked

```text
400 Bad Request
```

```json
{
  "detail": "Seat(s) already booked: S1."
}
```

---

## Duplicate Seat Numbers

```text
400 Bad Request
```

```json
{
  "seat_numbers": [
    "Duplicate seat numbers are not allowed."
  ]
}
```

---

## No Seats Selected

```text
400 Bad Request
```

```json
{
  "seat_numbers": [
    "This list may not be empty."
  ]
}
```

---

## Not Enough Seats Available

```text
400 Bad Request
```

```json
{
  "detail": "Not enough seats available."
}
```