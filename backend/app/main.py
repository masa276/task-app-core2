from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ★ modelsは必ず先に読み込む（SQLAlchemy対策）
from app.models import user, task

# ★ router読み込み
from app.api.routes import tasks, auth
from app.db.session import engine



user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

# =========================
# CORS設定
# =========================
origins = [
    "http://localhost:5173",   # Vite
    "http://localhost:3000",   # React
    "https://your-frontend.vercel.app"  # 本番フロント
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Router登録（ここが重要）
# =========================
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# =========================
# Root確認用
# =========================
@app.get("/")
def root():
    return {"message": "API running"}
