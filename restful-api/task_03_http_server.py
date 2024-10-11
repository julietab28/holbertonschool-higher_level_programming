#!/usr/bin/python3
import json
import http.server, socketserver

PORT = 8000

#esta es la api
class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

with socketserver.TCPServer(("", PORT), Server) as server:
    server.serve_forever()