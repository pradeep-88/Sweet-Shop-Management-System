from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base


class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), unique=True, index=True, nullable=False)

    category = Column(String(100), index=True, nullable=False)

    price = Column(Float, nullable=False)

    quantity = Column(Integer, nullable=False, default=0)
