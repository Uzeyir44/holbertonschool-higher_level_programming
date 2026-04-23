##Projects

###task_02_requests.py

- Create a function fetch_and_print_posts() that fetches all post from JSONPlaceholder.

 - Print the status code of the response i.e. Status Code: 200
 - If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
 - Iterate through the parsed JSON data and print out the titles of all the posts.

- Create a function fetch_and_save_posts() that fetches all post from JSONPlaceholder.

 - If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
 - Using Python's csv module, write this data into a CSV file called posts.csv with columns corresponding to the dictionary keys.