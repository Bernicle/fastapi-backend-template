from sqlalchemy import Column, Integer, String

from config.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(120), unique=True, nullable=False)
    hash_password = Column(String(128), nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    extension_name = Column(String)
    address = Column(String)
    mobile_number = Column(String(20), nullable=False)

Base.metadata.create_all(bind=engine)