from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import engine
from app.db.base import Base   # ★これ推奨

import app.models.user
import app.models.task

from app.api.routes import tasks, auth

app = FastAPI(title="Task Management API")

# ★テーブル作成（これが確実）
Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://your-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "API running"}
