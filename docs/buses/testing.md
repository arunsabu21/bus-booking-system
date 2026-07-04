# Buses API Testing

## GET /api/buses/

### Test Case 1

Description:

Retrieve all active buses.

Expected Result:

- Status Code: 200 OK
- Returns a list of active buses.

Result:

- Pass

---

## GET /api/buses/{bus_id}/

### Test Case 1

Description:

Retrieve an existing active bus.

Expected Result:

- Status Code: 200 OK
- Returns bus details.

Result:

- Pass

---

### Test Case 2

Description:

Retrieve a non-existing bus.

Expected Result:

- Status Code: 400 Bad Request
- Returns "Bus not found."

Result:

- Pass

---

### Test Case 3

Description:

Retrieve an inactive bus.

Expected Result:

- Status Code: 400 Bad Request
- Returns "Bus not found."

Result:

- Pass