from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session

from internal.repository.base import Base
from typing import Optional, List


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def __str__(self):
        return f'id: {self.id} ,email: {self.email}, hashed_password: {self.hashed_password}, is_active: {self.is_active}'