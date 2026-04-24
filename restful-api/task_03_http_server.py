#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == "/data"):
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
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found!")

def run(class_server=HTTPServer, class_handler=MyHandler):
    server_address = ('', 8000)
    httpd = class_server(server_address, class_handler)
    httpd.serve_forever()

run()