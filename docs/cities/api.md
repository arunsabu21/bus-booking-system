# Cities API

Base URL

```
/api/v1/cities/
```

---

## Get Cities

Returns all active cities.

### Endpoint

```
GET /api/v1/cities/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
[
  {
    "id": "c7b9b5d2-5c84-4b68-b6f4-d6d4d84f58b4",
    "name": "Chennai",
    "state": "Tamil Nadu"
  },
  {
    "id": "f4a2b95f-dc1f-4cf5-98b3-7d2d45d39b11",
    "name": "Bengaluru",
    "state": "Karnataka"
  }
]
```

---

## Get City Details

Returns details of a single active city.

### Endpoint

```
GET /api/v1/cities/{city_id}/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
{
  "id": "c7b9b5d2-5c84-4b68-b6f4-d6d4d84f58b4",
  "name": "Chennai",
  "state": "Tamil Nadu",
  "is_active": true,
  "created_at": "2026-07-04T10:30:00Z",
  "updated_at": "2026-07-04T10:30:00Z"
}
```

### Error Response (400 Bad Request)

```json
{
  "detail": "City not found."
}
```