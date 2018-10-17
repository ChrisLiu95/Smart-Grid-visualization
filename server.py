#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open("jsonfile.json",'r') as load_f:
          load_dict = json.load(load_f)
        # Write content as utf-8 data
        self.wfile.write(json.dumps(load_dict).encode('utf-8'))
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()