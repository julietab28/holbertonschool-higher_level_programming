#!/usr/bin/python3
import json
import http.server, socketserver

PORT = 8080

#esta es la api
class Server(http.server.BaseHTTPRequestHandler):
    dic_datos = {
        "name": "John", 
        "age": 30, 
        "city": "New York"
    }
    dic_info = {
        "version": "1.0",
        "description": "A simple API built with http.server"
    }

    json_datos = json.dumps(dic_datos) 
    json_info = json.dumps(dic_info)
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(self.json_datos.encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("OK", 'utf-8'))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(self.json_info.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))

with socketserver.TCPServer(("", PORT), Server) as server:
    server.serve_forever()