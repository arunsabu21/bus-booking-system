# Routes API Testing

## Get Available Routes

### Test Case 1 - Get all active routes

**Method**

```
http GET
```

**Endpoint**

```text
/api/routes/
```

**Headers**

None.

**Expected Status**

```text
200 OK
```

**Expected Result**

- Returns a list of active routes.
- Routes are ordered by creation date.
- Each route contains:
  - id
  - route_code
  - route_name
  - source_city
  - is_active
  - created_at
  - updated_at

---

### Test Case 2 - No active routes

**Expected Status**

```text
404 Not Found
```

**Expected Result**

```json
{
    "detail": "No routes found."
}
```