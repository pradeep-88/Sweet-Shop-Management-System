from pydantic import BaseModel


class SaleCreate(BaseModel):
    sweet_id: int
    quantity: int


class SaleOut(BaseModel):
    id: int
    sweet_id: int
    quantity: int
    sold_by: int

    class Config:
        from_attributes = True
