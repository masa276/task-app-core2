from fastapi import APIRouter
from app.core.security import create_token

router = APIRouter()

@router.post("/login")
def login():
    token = create_token({"user_id": 1})
    return {"access_token": token}
