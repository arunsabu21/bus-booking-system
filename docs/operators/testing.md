# Operators API Testing

## GET /api/operators/

### Test Case 1

Description:
Retrieve all active operators.

Expected Result:

- Status Code: 200 OK
- Returns a list of operators.

Result:

- Pass

---

## GET /api/operators/{operator_id}/

### Test Case 1

Description:
Retrieve an existing operator.

Expected Result:

- Status Code: 200 OK
- Returns operator details.

Result:

- Pass

---

### Test Case 2

Description:
Retrieve a non-existing operator.

Expected Result:

- Status Code: 400 Bad Request
- Returns "Operator not found."

Result:

- Pass

---

### Test Case 3

Description:
Retrieve an inactive operator.

Expected Result:

- Status Code: 400 Bad Request
- Returns "Operator not found."

Result:

- Pass
