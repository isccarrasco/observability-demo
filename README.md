# observability-demo

Demo for Observability with FastAPI and Prometheus

```shell
docker run \
  -p 9090:9090 \
  -v /PATH/TO/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

Run the FastAPI application

```shell
uvicorn app:app --reload --host 0.0.0.0 
```

host parameter is required to allow access from the dockerized prometheus 