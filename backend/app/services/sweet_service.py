from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetUpdate
from app.repositories.sweet_repo import SweetRepository


class SweetService:

    @staticmethod
    def create(db: Session, sweet_data: SweetCreate):
        sweet = Sweet(**sweet_data.dict())
        return SweetRepository.create(db, sweet)

    @staticmethod
    def list(
        db: Session,
        name: str | None,
        category: str | None,
        min_price: float | None,
        max_price: float | None,
        skip: int,
        limit: int,
    ):
        return SweetRepository.get_filtered(
            db=db,
            name=name,
            category=category,
            min_price=min_price,
            max_price=max_price,
            skip=skip,
            limit=limit,
        )

    @staticmethod
    def get(db: Session, sweet_id: int):
        sweet = SweetRepository.get_by_id(db, sweet_id)
        if not sweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sweet not found",
            )
        return sweet

    @staticmethod
    def update(db: Session, sweet_id: int, sweet_data: SweetUpdate):
        sweet = SweetRepository.get_by_id(db, sweet_id)
        if not sweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sweet not found",
            )

        for key, value in sweet_data.dict(exclude_unset=True).items():
            setattr(sweet, key, value)

        db.commit()
        db.refresh(sweet)
        return sweet

    @staticmethod
    def delete(db: Session, sweet_id: int):
        sweet = SweetRepository.get_by_id(db, sweet_id)
        if not sweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sweet not found",
            )

        SweetRepository.delete(db, sweet)
        return {"message": "Sweet deleted successfully"}
