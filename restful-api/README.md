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