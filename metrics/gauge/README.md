# Gauge Metric
- Used for recording a value that can go up or down

### Examples for Gauge usage
- Number of Items in Queue
- Temperature
- Current Memory usage

```bash
python3 gauge_metric.py

# Make calls to the server
 curl localhost:8001/?[1-10000]

# Check the last time a call succeded to that end point
time()-request_last_served
```