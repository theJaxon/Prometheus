```bash
# Start prometheus server wherever the prometheus.yml file is located
prometheus

# Start the python web server 
python3 counter_metric.py

# Make 10 requests to the hello world page to increase the counter
curl localhost:8001/?[1-10]

# Check the total number of calls
hello_world_total # Shows 10
```