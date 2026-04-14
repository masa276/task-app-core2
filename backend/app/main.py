from fastapi import FastAPI
from app.api.routes import auth, tasks

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(tasks.router, prefix="/tasks")

@app.get("/")
def root():
    return {"message": "API running"}
