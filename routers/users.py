from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from uuid import uuid4

router = APIRouter(
    prefix="/users",
    tags=["Users Service"]
)

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = "employee"

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    is_active: bool = True

fake_users_db = []

@router.get("/", response_model=List[User])
def get_users():
    return fake_users_db

@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate):
    new_user = user.model_dump()
    new_user["id"] = str(uuid4())
    new_user["is_active"] = True
    fake_users_db.append(new_user)
    return new_user