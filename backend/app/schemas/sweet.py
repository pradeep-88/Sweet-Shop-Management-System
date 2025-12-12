from pydantic import BaseModel
from typing import Optional


class SweetBase(BaseModel):
    name: str
    price: float
    quantity: int
    category: Optional[str] = None


class SweetCreate(SweetBase):
    pass


class SweetUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None


class SweetOut(SweetBase):
    id: int

    class Config:
        from_attributes = True
