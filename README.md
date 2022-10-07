# Prometheus
Learning Prometheus - An application used for Monitoring

![architecture](https://github.com/theJaxon/Prometheus/blob/main/etc/Architecture.jpeg)

### Config related notes
- Prometheus default port is `9090`
- Node Exporter default port is `9100`

### Terminologies
- Target: Object whose metrics are to be monitored
- Instance: Endpoint that can be scraped
- Job: Collection of `Targets/Instances` with the same purpose
- Alert Manager: Receives alerts from Prometheus Server and turns them into notifications
- Software Instrumentation: Help us to see what systems are doing, used to Integrate the applications with Prometheus

### Exporters
- When Instrumentation is not possible (Having no control over source code is an example) then an exporter can be used to do the job
- An exporter fetches statistics from another non-prometheus system, then using a client library these statistics can be turned into metrics
- Exporters start a **Web Server** that exposes a `URL` and have that URL display the metrics

#### Node Exporter
- Official exporter for **Hardware and Kernel** related Metrics
- Provides Metrics like `CPU, Memory, Disk Space, Disk IO and Network Bandwidth`

### Functions
- `rate` functions calculates how fast a counter is increasing per second

---

### Node Exporter and Promethues Config
- By default prometheus checks for `prometheus.yml` file in the current directory to load its configuration from
```yaml
global:
  scrape_interval: 10s
scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets:
          - 'localhost:9090'
  - job_name: node_exporter
    static_configs:
      - targets:
          - 'localhost:9100'
```

---

- `process_resident_memory_bytes{job="job_name"}` can be used to track the memory consumption of each job (prometheus or node_exporter in this case)
- `up` shows us whether the job is running or not, since both node_exporter and prometheus are running both show a value of 1
---

### Alerting Example
- From Prometheus Up & Running 2nd Edition
- Start by exiting node_exporter process
- The configuration checks for a minute if the node_exporter job is `up` or not, if it's not then an alert is sent
