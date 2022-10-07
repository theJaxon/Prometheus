# Prometheus
Learning Prometheus - An application used for Monitoring

![architecture](https://github.com/theJaxon/Prometheus/blob/main/etc/Architecture.jpeg)

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
