from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)

    products = relationship("Product", back_populates="supplier")
