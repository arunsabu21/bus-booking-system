# Cities API Testing

## GET /api/cities/

### Test Case 1

Description:

Retrieve all active cities.

Expected Result:

- Status Code: 200 OK
- Returns a list of active cities.

Result:

- Pass

---

## GET /api/cities/{city_id}/

### Test Case 1

Description:

Retrieve an existing active city.

Expected Result:

- Status Code: 200 OK
- Returns city details.

Result:

- Pass

---

### Test Case 2

Description:

Retrieve a non-existing city.

Expected Result:

- Status Code: 400 Bad Request
- Returns "City not found."

Result:

- Pass

---

### Test Case 3

Description:

Retrieve an inactive city.

Expected Result:

- Status Code: 400 Bad Request
- Returns "City not found."

Result:

- Pass