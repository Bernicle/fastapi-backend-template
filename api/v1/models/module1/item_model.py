from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .....config.database import Base, engine

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
