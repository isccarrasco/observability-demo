from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator, metrics

app = FastAPI()

Instrumentator().add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=False,
        should_include_status=True,
        metric_namespace="a",
        metric_subsystem="b",
    )
).add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=False,
        should_include_status=True,
        metric_namespace="namespace",
        metric_subsystem="subsystem",
    )
).instrument(app).expose(app)


@app.get("/")
def index():
    return {"status": "up"}
