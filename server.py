import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "/1.html"
        
        return super().do_GET()

if __name__ == "__main__":
    server_address = ("", 80)  # Listen on port 80
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving on port 80...")
    httpd.serve_forever()
