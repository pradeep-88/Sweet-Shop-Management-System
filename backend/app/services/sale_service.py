from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.sale_repo import SaleRepository
from app.repositories.sweet_repo import SweetRepository
from app.models.sale import Sale


class SaleService:

    @staticmethod
    def sell(db: Session, sweet_id: int, quantity: int, sold_by: int):
        sweet = SweetRepository.get_by_id(db, sweet_id)

        if not sweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sweet not found",
            )

        if sweet.quantity < quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient stock",
            )

        # Reduce stock
        sweet.quantity -= quantity
        db.commit()
        db.refresh(sweet)

        sale = Sale(
            sweet_id=sweet_id,
            quantity=quantity,
            sold_by=sold_by,
        )
        return SaleRepository.create(db, sale)
