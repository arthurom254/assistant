import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

def getHtml(prompt):
    return f"""
    <html>
        <head>
            <title>Generate Image</title>
        </head>
        <body>
            <h1>{prompt}</h1>
            <img src='http://192.168.127.77:8000/img.png'/>
        </body>
    </html>
    """

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_content = getHtml()
        self.wfile.write(html_content.encode("utf-8"))
        # self.server.shutdown()  

def start_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

webbrowser.open("http://localhost:8000")

