from app.db.base import Base
from app.db.session import engine

# ★これが重要（必ずモデルを読み込む）
from app.models import user, task

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done")
