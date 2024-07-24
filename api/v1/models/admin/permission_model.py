from sqlalchemy import Column, Integer, String, Float

from config.database import Base, engine

class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    module = Column(String, nullable=False)
    submodule = Column(String, nullable=False)
    permissions = Column(String, nullable=False)
    
Base.metadata.create_all(bind=engine)