import http.server
import socketserver
import os
from pathlib import Path

# Set the working directory to the location of this script
# This ensures that the server serves files from the 'website' directory
web_dir = Path(__file__).parent
os.chdir(web_dir)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("🎨 Theme showcase running at http://localhost:" + str(PORT))
    print("Navigate to http://localhost:8000/index.html in your browser.")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever() 