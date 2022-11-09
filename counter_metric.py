import http.server
from prometheus_client import start_http_server, Counter 

REQUEST_COUNT = Counter('app_request_counts', 'Total HTTP Request Count', ['python_custom_app', 'endpoint'])

class HandleRequests(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    # REQUEST_COUNT.inc()
    REQUEST_COUNT.labels('get_function', self.path).inc()
    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()
    self.wfile.write(bytes("<html><head><title></title></head><body style='color:#333;margin-top:30px;'><center><h2>Welcome to Prometheus-Python application</center></h2></html>","utf-8"))
    self.wfile.close

if  __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(5001)
  server = http.server.HTTPServer(('134.122.70.44',5000), HandleRequests)
  server.serve_forever()
