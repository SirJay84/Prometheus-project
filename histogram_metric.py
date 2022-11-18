import http.server
import time
from prometheus_client import start_http_server, Histogram, Gauge

REQUEST_LATENCY_TIME = Histogram('request_latency_time', 'Response latency time in seconds')
REQUEST_IN_PROGRESS = Gauge('request_in_progress', 'Number of Live Request on Application')

class HandleRequests(http.server.BaseHTTPRequestHandler):
  @REQUEST_LATENCY_TIME.time()
  @REQUEST_IN_PROGRESS.track_inprogress()
  def do_GET(self):
    self.send_response(200)
    time.sleep(1)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()
    self.wfile.write(bytes("<html><head><title></title></head><body style='color:#333;margin-top:30px;'><center><h2>Welcome to Prometheus-Python application</center></h2></html>","utf-8"))
    self.wfile.close
    

if  __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(5001)
  server = http.server.HTTPServer(('134.122.70.44',5000), HandleRequests)
  server.serve_forever()
