# Trips API Testing

## Get Available Trips

### Test Case 1 - Get all active trips

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/trips/
```

**Headers**

None

**Expected Status**

```text
200 OK
```

**Expected Result**

- Returns a list of active trips.
- Trips are ordered by travel date.
- Each trip contains:
    - id
    - route
    - bus
    - travel_date
    - departure_time
    - arrival_time
    - fare
    - available_seats
    - status

---

### Test Case 2 - No active trips

**Expected Status**

```text
404 Not Found
```

**Expected Result**

```json
{
    "detail": "Trip not found."
}
```

---

## Get Trip Details

### Test Case 1 - Get Trip details by valid ID

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/trips/<trip_id>/
```

**Headers**

None

**Expected Status**

```text
200 OK
```

**Expected Result**

- Returns the requested active trip details.
- Response Contains:
    - id
    - route
    - bus
    - travel_date
    - departure_time
    - arrival_time
    - fare
    - available_seats
    - status
    - is_active
    - created_at
    - updated_at

---

### Test Case 2 - Trip does not exist

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/trips/<non_existing_trip_by_id>/
```

**Headers**

None

**Expected Status**

```text
404 Not Found
```

**Expected Result**

```json
{
    "detail": "Trip not found."
}
```

---

### Test Case 3 - Invalid Trip ID

**Method**

```http
GET
```

**Endpoint**

```text
/api/v1/trips/invalid-uuid/
```

**Headers**

None

**Expected Status**

```text
404 Not Found
```

**Expected Result**

- Request is rejected because the route ID is not a valid UUID.
- The request does not reach the view.