# JSONPlaceholder API Testing Exercise

## 📌 Overview

This Home exercise includes a set of automated tests for the [JSONPlaceholder](https://jsonplaceholder.typicode.com) RESTful API,
It covers full CRUD operations (`GET`, `POST`, `PUT`, `DELETE`) with both positive and negative test cases, response data validation, and status code assertions.

## 🎯 Test Objectives


- ✅ Ensure appropriate status codes (`200`, `201`, `404`) are returned for valid and invalid inputs.
- ✅ Validate the structure and type of JSON response fields (`userId`, `id`, `title`, `body`).
- ✅ Verify successful retrieval of all posts and individual posts by valid ID.
- ✅ Test POST endpoint with complete and incomplete payloads.
- ✅ Test PUT endpoint with full data and partial data (missing fields).
- ✅ Test DELETE endpoint functionality for existing, non-existent, and invalid post IDs.
- ✅ Include both positive and negative edge cases across all endpoints to evaluate API robustness.



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

1. Open a new empty Project(Pycharm,Vscode), In Terminal Clone the Repository
   ```bash
   git clone https://github.com/Ameerm98/JSONPlaceholder-API-Testing.git
2. Enter JSONPlaceholder-API-Testing directory 
   ```bash
   cd JSONPlaceholder-API-Testing
3. Make sure Python and `pip` are installed on your system.
4. Create a clean virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate     # Mac: source venv/bin/activate      
   
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
6. Run the tests normally using:
   ```bash
    pytest

📊 How to Generate Allure Reports(Bonus)

🔹 Mac\Linux (Homebrew)
   ```bash 
   brew install allure
```
🔹 Windows

Download Allure from: https://allurereport.org/docs/install-for-windows/

🧪 Run with Allure
   ```bash
   pytest --alluredir=allure-results
   allure generate allure-results --clean -o allure-report
   allure serve allure-results
   ```
This will generate and open a rich HTML report with:

✔ - Test results summary

🔍- Test details with steps and status

⚠️ Interesting Findings
- JSONPlaceholder is a fake API – It simulates creation, updates, and deletion, but does not persist any data.

- Sending a PUT request with an ID outside the range 1–100 results in a 500 Internal Server Error, instead of a more appropriate status like 404 Not Found or 400 Bad Request.

- The API accepts incomplete or empty payloads (POST/PUT) and still returns success (201 Created or 200 OK) – which wouldn’t be acceptable for production-grade APIs.



💡 Suggestions for Improving the API

 - Implement real state changes (i.e., persist POST, DELETE, etc.) for better testing.

 - Return 400 Bad Request for invalid input types or missing fields during POST/PUT.
