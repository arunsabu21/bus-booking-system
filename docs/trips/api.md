# Trips API

## Get Available Trips

**Base URL**

```
api/v1/trips/
```

---

## Get Trips

Returns a list of all active trips ordered by travel date and departure time.

**Endpoint**

```http
GET /api/v1/trips/
```

**Authentication**

None.

**Permission**

AllowAny

**Success Response (200 OK)**

```json
[
  {
    "id": "2ea879b3-8719-4747-83fb-75df0bb13a39",
    "route": "Chennai → Bengaluru",
    "bus": "KSRTC301",
    "travel_date": "2026-07-07",
    "departure_time": "21:00:00",
    "arrival_time": "05:30:00",
    "fare": "850.00",
    "available_seats": 36,
    "status": "SCHEDULED"
  },
  {
    "id": "f9cf2f88-0fba-41e1-93fa-97d625c432d9",
    "route": "Bengaluru → Hyderabad",
    "bus": "KSRTC415",
    "travel_date": "2026-07-07",
    "departure_time": "22:00:00",
    "arrival_time": "06:00:00",
    "fare": "1200.00",
    "available_seats": 30,
    "status": "SCHEDULED"
  }
]
```

---

## Get Trip Details

Returns details of a single active trip.

**Endpoint**

```http
GET /api/v1/trips/{trip_id}/
```

**Authentication**

None

**Permission**

AllowAny

**Success Response (200 OK)**

```json
{
  "id": "2ea879b3-8719-4747-83fb-75df0bb13a39",
  "route": "Chennai → Bengaluru",
  "bus": "KSRTC301",
  "travel_date": "2026-07-07",
  "departure_time": "21:00:00",
  "arrival_time": "05:30:00",
  "fare": "850.00",
  "available_seats": 36,
  "status": "SCHEDULED",
  "is_active": true,
  "created_at": "2026-07-06T20:37:32.010359+05:30",
  "updated_at": "2026-07-06T20:37:32.010386+05:30"
}
```

**Error Response (404 Not Found)**

```json
{
    "detail": "Trip not found."
}
```

