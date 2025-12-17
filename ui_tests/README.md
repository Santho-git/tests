<h2> ReqRes API Testing using Pytest </h2>

<h3>Overview:</h3>
         This project demonstrates API testing using Python’s pytest framework and the requests library against the publicly available ReqRes API. 
         The goal is to validate successful responses, response content, and error handling behavior of RESTful APIs.

<h3>Tools & Technologies:</h3>

  1. Python 
  
  2. pytest – Test framework
     
  3. requests – HTTP client library for API calls
     
  4. PyCharm – IDE used for execution

<h3>API Under Test: </h3>
Base URL: https://reqres.in/api

<h3>APIs covered:</h3>

* GET /users?page=2
  
* GET /users/2
  
* POST /login

</h3>Test Cases Implemented:</h3>

1. Validate successful response for listing users
    * Sends a GET request to retrieve users
    * Verifies HTTP status code 200 OK

2. Validate response content for a single user
    * Fetches user data for user ID 2
    * Validates that:
      * Response contains data key
      * User ID returned matches the requested ID

3. Validate error handling for invalid login
    * Sends a POST request with missing password
    * Verifies:
      * HTTP status code 400 Bad Request
      * Presence of error message in response

<h3>Handling Cloudflare Restriction:</h3>

  * The ReqRes public API is currently protected by Cloudflare CAPTCHA, which blocks automated API requests from tools such as pytest or Postman and returns a 403 Forbidden response.
    
  * To handle this gracefully:
    * Tests detect a 403 status code
    * Blocked tests are skipped using pytest.skip()
    * This ensures test logic remains correct while acknowledging environmental limitations
    * The test cases reflect the expected API behavior as per official ReqRes documentation.

