import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "/1.html"
        
        if self.path == "/1.html":
            self.inject_file_list()

        return super().do_GET()

    def inject_file_list(self):
        """Modify 1.html to include a hidden (commented out) list of sorted HTML files."""
        html_files = sorted(
            [f for f in os.listdir(".") if f.endswith(".html") and f.split('.')[0].isdigit()],
            key=lambda x: int(x.split('.')[0])
        )

        file_list_html = "<!--\n<ul>\n" + "".join(f"  <li>{file}</li>\n" for file in html_files) + "</ul>\n-->"

        with open("1.html", "r") as f:
            content = f.read()

        # Ensure there's only one file list by replacing it if already present
        if "<!--\n<ul>" in content:
            content = content.split("<!--\n<ul>")[0]

        # Add the hidden file list before `</body>`
        new_content = content.replace("</body>", file_list_html + "</body>")

        with open("1.html", "w") as f:
            f.write(new_content)

if __name__ == "__main__":
    server_address = ("", 80)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving on port 80...")
    httpd.serve_forever()
