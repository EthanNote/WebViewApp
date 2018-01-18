import webview
import sys
import threading
import time

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer

"""
This example demonstrates how a trivial application can be built using a HTTP server combined with a web view.
"""

class UIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('<script>document.write("Hello, world!")</script>'.encode())

def start_server():
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass = HTTPServer
    Protocol = "HTTP/1.0"
    port = 23948
    server_address = ('127.0.0.1', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, UIHandler)
    httpd.serve_forever()

def other_job():
    time.sleep(10)
    webview.evaluate_js('alert("job")')

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    threading.Thread(target=other_job).start()

    webview.create_window("My first HTML5 application", "http://127.0.0.1:23948")

    # do clean up procedure and destroy any remaining threads after the window is destroyed
    sys.exit()