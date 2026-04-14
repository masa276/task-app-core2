from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import user, task

from app.api.routes import tasks, auth  # ★追加

app = FastAPI()

# 🔥 CORS設定
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

# ★★★ これが超重要（API登録）
app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API running"}
