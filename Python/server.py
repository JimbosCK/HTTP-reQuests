from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
       
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response_body = "Hello " + self.headers['name']
        self.wfile.write(response_body.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyHttpRequestHandler):
    server_address = ('', 3000)
    httpd = server_class(server_address, handler_class)
    print("Running server on port : 3000")
    httpd.serve_forever()

run()