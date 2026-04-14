from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Taskとのリレーション
    tasks = relationship(
        "Task",  # ← 文字列参照（重要）
        back_populates="user",
        cascade="all, delete-orphan"
    )
