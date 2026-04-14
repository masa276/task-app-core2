from app.db.session import Base, engine

# モデルを読み込む（超重要）
from app.models.user import User
from app.models.task import Task

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
