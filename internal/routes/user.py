from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from internal.repository.base import get_db
from internal.services.users import get_user_by_email, create_user, get_users, get_user
from internal.services.items import create_user_item
from models.user_model import User, UserCreate
from models.item_model import ItemCreate, Item

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"descriptions": "Not found"}}
)


@router.post("/", response_model=User)
def create_single_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/items/", response_model=Item)
def create_item_for_user(
        user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)
