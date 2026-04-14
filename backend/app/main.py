from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 CORS設定
origins = [
    "http://localhost:5173",  # 開発用（Vite）
    "http://localhost:3000",  # React別環境
    "https://your-frontend.vercel.app"  # 本番（重要）
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # 許可するドメイン
    allow_credentials=True,
    allow_methods=["*"],     # GET/POST/PUT/DELETE全部OK
    allow_headers=["*"],     # 全ヘッダー許可
)

@app.get("/")
def root():
    return {"message": "API running"}
