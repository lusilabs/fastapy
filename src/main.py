from typing import Optional
from rq import Queue
from redis import Redis
from fastapi import FastAPI, HTTPException
from rq.job import Job
from jobs import runTask

app = FastAPI()

redis_conn = Redis(host='redis', port=6379)
q = Queue('default_queue_name', connection=redis_conn)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/jobs", status_code=201)
def start_task():
    job = q.enqueue(runTask)
    return {'jobID': job.id}


@app.get("/jobs/{job_id}")
def read_item(job_id: str, q: Optional[str] = None):
    job = Job.fetch(job_id, connection=redis_conn)
    return {"result": job.result}