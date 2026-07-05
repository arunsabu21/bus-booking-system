# Routes API

## Get Available Routes

**Base URL**

```
api/routes/
```

---

## Get Routes

Returns a list of all active routes ordered by creation date.

### Endpoint

```
GET /api/routes/
```
### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
[
  {
    "id": "93303d1b-f7c3-4db6-95a0-bb5368c21ea8",
    "route_code": "R001",
    "route_name": "Chennai → Bengaluru",
    "source_city": "d89362eb-612d-48a0-9c52-97d7506cbd37",
    "is_active": true,
    "created_at": "2026-07-05T20:53:37.227250+05:30",
    "updated_at": "2026-07-05T20:53:37.227287+05:30"
  }
]
```

