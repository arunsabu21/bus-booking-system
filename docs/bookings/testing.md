# Bookings API Testing

## Get All Bookings

### Test Case 1 - Get all bookings

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/bookings/
```

**Headers**

None

**Expected Status**

```text
200 OK
```

**Expected Result**

- Status Code 200 OK
- Returns only the authenticated user's bookings.

---

### Test Case 2 - Authenticated user without bookings

**Expected Result**

- Status Code 200 OK
- Returns an empty list

**Example**

```json
[]
```

---

### Test Case 3 - Request without JWT Token

**Expected Result**

```text
401 Unauthorized
```

---

## Endpoint 2

```http
GET /api/v1/bookings/{booking_id}/
```

**Authentication Required**

---

### Test Case 1 - Authenticated user requests their own booking

**Expected Result**

- Status Code 200 OK
- Returns booking details

---

### Test Case 2 - Authenticated user requests another user's booking

**Expected Result**

- Status Code 404 Not Found

---

### Test Case 3 - Invalid booking ID

**Expected Result**

- Status Code 404 Not Found

---

### Test Case 4 - Request without JWT Token

**Expected Result**

- Status Code 401 Unauthorized

---

## Create Booking

**Method**

```http
POST
```

**Endpoint**

```text
/api/v1/bookings/create/
```

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

**Expected Result**

- Status Code: 201 Created
- Booking created successfully
- Booking reference generated
- Total amount calculated
- Available seats reduced

---

### Test Case 1 - Invalid Trip

**Body**

```json
{
    "trip": "00000000-000000-000000-0000000000",
    "seat_count": 2
}
```

**Expected**

- 404 Not Found

---

### Test Case 2 - Seat count = 0

**Body**

```json
{
    "trip": "00000000-000000-000000-0000000000",
    "seat_count": 0
}
```

**Expected**

- 400 Bad Request


