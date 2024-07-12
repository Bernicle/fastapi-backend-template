from sqlalchemy import Column, Integer, String, Float

from config.database import Base, engine

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

Base.metadata.create_all(bind=engine)