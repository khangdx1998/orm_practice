from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal.repository.base import get_db
from internal.services.items import get_items
from models.item_model import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"descriptions": "Not found"}}
)


@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items
