# JSONPlaceholder API Test Suite

## 📌 Overview

This Home exercise includes a set of automated tests for the [JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API,
built using `Python`, `requests`, and `pytest`. 
It covers full CRUD operations (`GET`, `POST`, `PUT`, `DELETE`) with both positive and negative test cases, response data validation, and status code assertions.

---

## 🔧 Tools & Libraries Used

- **Python 3.10+** – Core language for scripting.
- **[Requests](https://docs.python-requests.org/)** – Simple HTTP client for API requests.
- **[Pytest](https://docs.pytest.org/)** – Testing framework with clean syntax and powerful features.
- **http.HTTPStatus** – Built-in enum for readable HTTP status codes.

**Why these tools?**  
They are lightweight, widely adopted in API testing, and allow fast prototyping with easy-to-read syntax.

---

## 🚀 How to Run the Tests

1. Make sure Python and `pip` are installed on your system.
2. Install dependencies:
   ```bash
   pip install requests pytest
3. Run the tests using:
   ```bash
    pytest test_jsonplaceholder.py -v
   
⚠️ Challenges & Interesting Findings

JSONPlaceholder is a fake API – It simulates creation/deletion but does not persist data.

For real-world APIs, further validations (like confirming deletion via GET) would need actual persistence.


💡 Suggestions for Improving the API

Implement real state changes (i.e., persist POST, DELETE, etc.) for better testing.
Return 400 Bad Request for invalid input types or missing fields during POST/PUT.
