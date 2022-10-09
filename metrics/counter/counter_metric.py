import http.server
from prometheus_client import start_http_server, Counter

# Use Counter Metric
REQUESTS = Counter(
    # hello_world is the counter name
    # "The total number of hello worlds requests so far." is the help string that appears on /metrics page to get a better idea about the meaning of the metric
    "hello_world",
    "The total number of hello worlds requests so far.",
)


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    # Start HTTP server on port 8000 to serve metrics to Prometheus
    # Metrics can be viewed via localhost:8000
    start_http_server(8000)

    # Whenever a call to localhost:8081 happens, MyHandler is invoked
    server = http.server.HTTPServer(("localhost", 8001), MyHandler)
    server.serve_forever()
