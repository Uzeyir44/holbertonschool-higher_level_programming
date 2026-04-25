##Projects

###task_02_requests.py

- Create a function fetch_and_print_posts() that fetches all post from JSONPlaceholder.

 - Print the status code of the response i.e. Status Code: 200
 - If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
 - Iterate through the parsed JSON data and print out the titles of all the posts.

- Create a function fetch_and_save_posts() that fetches all post from JSONPlaceholder.

 - If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
 - Using Python's csv module, write this data into a CSV file called posts.csv with columns corresponding to the dictionary keys.

 ###task_03_http_server.py

- Setting Up a Basic HTTP Server:

 - Use the http.server module to set up a simple HTTP server. Start by creating a subclass of http.server.BaseHTTPRequestHandler.
 - Implement the do_GET method to handle GET requests. Within this method, send a simple text response back to the client: "Hello, this is a simple API!".
 - Start the server on a specific port (8000) and test it by visiting http://localhost:8000 in your browser or using curl.

- Serving JSON Data:

 - Modify the do_GET method in your server class to serve a sample JSON data when the endpoint /data is accessed.
 - You should return a simple dataset: {"name": "John", "age": 30, "city": "New York"}.
 - Ensure that the correct content type (application/json) header is set in the response.

- Handling Different Endpoints:

 - Add an /status endpoint to check the API status. It shoud return OK.
 - Implement error handling. If the user tries to access an undefined endpoint, return a 404 Not Found status with an appropriate message.

###task_04_flask.py

- Setting Up Flask:

 - Install Flask using pip: pip install Flask.
 - Create a new Python file and import Flask: from flask import Flask.
 - Instantiate a Flask web server from the Flask module: app = Flask(__name__).

- Creating Your First Endpoint:

 - Define a route for the root URL ("/") and create a function (def home():) to handle this route. Within the function, return a string: "Welcome to the Flask API!".
 - Run the Flask development server with: if __name__ == "__main__": app.run().
 - Visit http://localhost:5000 in your browser or use curl to see the message.

- Serving JSON Data:

 - Import the jsonify function from Flask: from flask import jsonify.
 - Create a new route /data and associate a function with it. Inside this function, return a JSON response using jsonify(). This should return a list of all the usernames stored in the API.
 - Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
 - Example dictionary: users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
 - NOTE: To avoid problem with the checker, do not include your testing data when pushing your code.

- Expanding Your API:

 - Add a few more endpoints to simulate different functionalities:
 - /status: It should return OK.
 - /users/<username>: Returns the full object corresponding to the provided username. (Hint: Use Flask's dynamic route feature)
 - If the user does not exist, return a 404 with {"error": "User not found"}.

- Handling POST Requests:

 - Import the request object from Flask: from flask import request.
 - Create a new route /add_user that accepts POST requests.
 - This route should:
  - Parse the incoming JSON data. Example data: {"username": "john", "name": "John", "age": 30, "city": "New York"}
  - Add the new user to the users dictionary using username as the key.
  - Return a confirmation message with the added user's data.
  - If the request body is not valid JSON, return 400 with {"error":"Invalid JSON"}.
  - If username is missing, return 400 with {"error":"Username is required"}.
  - If username already exists, return 409 with {"error":"Username already exists"}.

  ###task_05_basic_security.py

- Basic Authentication:
 - Install Flask-HTTPAuth:
  - Run: pip install Flask-HTTPAuth.
 - Set up Basic HTTP Authentication:
  - Create a list of users and their hashed passwords.
  - Use the werkzeug.security library for password hashing and verification.
 - Protect Routes with Basic Authentication:
  - Use the @auth.login_required decorator to protect certain routes.
- Token-based Authentication with JWT:
 - Install Flask-JWT-Extended:
  - Run: pip install Flask-JWT-Extended.
 - Set up JWT-based Authentication:
  - Use a secret key for token generation and validation.
  - Create a route /login where users can log in with their credentials and receive a JWT token.
 - Protect Routes with JWT Tokens:
  - Use the @jwt_required() decorator to protect certain routes.
- Implement Role-based Access Control:
  - Add roles (e.g., admin, user) to your users.
  - Create routes that should only be accessible to certain roles.
  - Implement checks to ensure the user's role matches the required role for accessing specific routes.