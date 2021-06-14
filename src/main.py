from typing import Optional
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from rq import Queue
from redis import Redis
from fastapi import FastAPI, HTTPException, status
from rq.job import Job
from jobs import runTask
from account.users import Token, UserInDB, User, authenticate_user, create_access_token, get_current_active_user, oauth2_scheme, \
    fake_users_db, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta


app = FastAPI()
redis_conn = Redis(host='redis', port=6379)
q = Queue('default_queue_name', connection=redis_conn)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {'success': 'true', 'the_token': token}

@app.post("/jobs", status_code=201)
def start_task():
    job = q.enqueue(runTask)
    return {'jobID': job.id}


@app.get("/jobs/{job_id}")
def read_item(job_id: str, q: Optional[str] = None):
    job = Job.fetch(job_id, connection=redis_conn)
    return {"result": job.result}