# Operators API

Base URL

```
/api/v1/operators/
```

---

## Get Operators

Returns all active bus operators.

### Endpoint

```
GET /api/v1/operators/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
[
  {
    "id": "3d3b5d2c-6f0b-4b29-9d6c-a4a2d7b4b6d1",
    "company_name": "KSRTC",
    "company_code": "KSRTC"
  },
  {
    "id": "b8ef6bb0-d4fd-46e4-9c7d-1b29d7f20a56",
    "company_name": "APSRTC",
    "company_code": "APSRTC"
  }
]
```

---

## Get Operator Details

Returns details of a single active operator.

### Endpoint

```
GET /api/v1/operators/{operator_id}/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
{
  "id": "3d3b5d2c-6f0b-4b29-9d6c-a4a2d7b4b6d1",
  "company_name": "KSRTC",
  "company_code": "KSRTC",
  "support_email": "support@ksrtc.in",
  "support_phone": "9876543210",
  "headquarters": "Bengaluru",
  "is_active": true,
  "created_at": "2026-07-03T09:00:00Z",
  "updated_at": "2026-07-03T09:00:00Z"
}
```

### Error Response (400 Bad Request)

```json
{
  "detail": "Operator not found."
}
```