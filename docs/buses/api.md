# Buses API

Base URL

```
/api/v1/buses/
```

---

## Get Buses

Returns all active buses.

### Endpoint

```
GET /api/v1/buses/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
[
  {
    "id": "1f5668be-466f-42e4-9afb-975d9dfc6006",
    "operator": "KSRTC",
    "bus_number": "KSRTC301",
    "bus_name": "Volvo 9600",
    "bus_type": "AC_SLEEPER",
    "total_seats": 36
  }
]
```

---

## Get Bus Details

Returns details of a single active bus.

### Endpoint

```
GET /api/v1/buses/{bus_id}/
```

### Authentication

None

### Permission

AllowAny

### Success Response (200 OK)

```json
{
  "id": "1f5668be-466f-42e4-9afb-975d9dfc6006",
  "operator": "KSRTC",
  "bus_number": "KSRTC301",
  "registration_number": "KA01AB1234",
  "bus_name": "Volvo 9600",
  "bus_type": "AC_SLEEPER",
  "total_seats": 36,
  "is_active": true,
  "created_at": "2026-07-04T12:00:00Z",
  "updated_at": "2026-07-04T12:00:00Z"
}
```

### Error Response (400 Bad Request)

```json
{
  "detail": "Bus not found."
}
```