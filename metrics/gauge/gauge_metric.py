import http.server, time
from prometheus_client import start_http_server, Gauge

IN_PROGRESS = Gauge(
    "hello_worlds_in_progress", "The Number of Hello Worlds in Progress."
)
LAST_SERVED = Gauge(
    "request_last_served", "Time at which the application was last served."
)


class MyHandler(http.server.BaseHTTPRequestHandler):
    @IN_PROGRESS.track_inprogress()
    def do_GET(self):
        time.sleep(5)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        LAST_SERVED.set_to_current_time()


if __name__ == "__main__":
    # Start HTTP server on port 8000 to serve metrics to Prometheus
    # Metrics can be viewed via localhost:8000
    start_http_server(8000)

    # Whenever a call to localhost:8081 happens, MyHandler is invoked
    server = http.server.HTTPServer(("localhost", 8001), MyHandler)
    server.serve_forever()
