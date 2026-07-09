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

```text
Authorization: Bearer <access_token>
```

**Expected Status**

```text
200 OK
```

**Expected Result**

- Status Code 200 OK
- Returns only the authenticated user's bookings.
- Returns booked seat numbers.

---

### Test Case 2 - Authenticated user without bookings

**Expected Result**

- Status Code 200 OK
- Returns an empty list.

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

## Get Booking Details

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/bookings/{booking_id}/
```

**Authentication Required**

---

### Test Case 1 - Authenticated user requests their own booking

**Expected Result**

- Status Code 200 OK
- Returns booking details including selected seat numbers.

---

### Test Case 2 - Authenticated user requests another user's booking

**Expected Result**

- Status Code 404 Not Found

---

### Test Case 3 - Invalid Booking ID

**Expected Result**

- Status Code 404 Not Found

---

### Test Case 4 - Request without JWT Token

**Expected Result**

- Status Code 401 Unauthorized

---

## Create Booking

### Test Case 1 - Successful Booking

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

**Body**

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_numbers": [
    "S1",
    "S2"
  ]
}
```

**Expected Result**

- Status Code 201 Created
- Booking created successfully.
- Booking reference generated.
- SeatBooking records created.
- Available seats reduced.
- Returns selected seat numbers.

---

### Test Case 2 - Invalid Trip

**Body**

```json
{
  "trip": "00000000-0000-0000-0000-000000000000",
  "seat_numbers": [
    "S1"
  ]
}
```

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 3 - Empty Seat List

**Body**

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_numbers": []
}
```

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 4 - Duplicate Seat Numbers

**Body**

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_numbers": [
    "S1",
    "S1"
  ]
}
```

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 5 - Already Booked Seat

**Body**

```json
{
  "trip": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "seat_numbers": [
    "S1"
  ]
}
```

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 6 - Not Enough Seats Available

**Body**

Select more seats than the trip has available.

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 7 - Request Without JWT Token

**Expected Result**

- Status Code 401 Unauthorized

---

## Cancel Booking

### Test Case 1 - Successfully Cancel Booking

**Method**

```http
PATCH
```

**Endpoint**

```text
/api/v1/bookings/{booking_id}/cancel/
```

**Expected Result**

- Status Code 200 OK
- Booking status updated to `CANCELLED`.
- Trip available seats increased.
- Associated seat bookings removed (or released, depending on your implementation).

---

### Test Case 2 - Cancel Already Cancelled Booking

**Expected Result**

- Status Code 400 Bad Request

---

### Test Case 3 - Invalid Booking ID

**Expected Result**

- Status Code 404 Not Found

---

### Test Case 4 - Request Without JWT Token

**Expected Result**

- Status Code 401 Unauthorized