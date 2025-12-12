from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.sweet import Sweet


class SweetRepository:

    @staticmethod
    def create(db: Session, sweet: Sweet) -> Sweet:
        db.add(sweet)
        db.commit()
        db.refresh(sweet)
        return sweet

    @staticmethod
    def get_filtered(
        db: Session,
        name: str | None = None,
        category: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        skip: int = 0,
        limit: int = 10,
    ):
        query = db.query(Sweet)

        if name:
            query = query.filter(Sweet.name.ilike(f"%{name}%"))

        if category:
            query = query.filter(Sweet.category == category)

        if min_price is not None:
            query = query.filter(Sweet.price >= min_price)

        if max_price is not None:
            query = query.filter(Sweet.price <= max_price)

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, sweet_id: int):
        return db.query(Sweet).filter(Sweet.id == sweet_id).first()

    @staticmethod
    def delete(db: Session, sweet: Sweet):
        db.delete(sweet)
        db.commit()
