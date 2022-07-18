from sqlalchemy.orm import Session
from internal.repository.user import User
from models.user_model import UserCreate
from typing import List, Optional


def get_user(db: Session, user_id: int) -> Optional[List[User]]:
    query = db.query(User).filter(User.id == user_id).first()
    print(query)
    return query


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> User:
    fake_hashed_password = user.password + "neurotrophically"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
