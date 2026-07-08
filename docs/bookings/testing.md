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

