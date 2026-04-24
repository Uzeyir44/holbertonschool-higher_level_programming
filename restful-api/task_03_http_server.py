#!/usr/bin/python3
"""
This module contains MyHandler class and run function
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    This class inherits from BaseHTTPRequestHandler and overwtites
    do_GET method

    methods:
        do_GET: handles the request-response process
    """
    def do_GET(self):
        """
        This function send different data to the web-page regarding endpoints
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif (self.path == "/data"):
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data).encode()
            self.send_response(200)

            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json_data)
        elif (self.path == "/status"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(class_server=HTTPServer, class_handler=MyHandler):
    """
    This function starts web server in 8000 localhost

    Args:
        class_server: the main server
        class_handler: class that handles all requests and responses
    """
    server_address = ('', 8000)
    httpd = class_server(server_address, class_handler)
    httpd.serve_forever()

run()
