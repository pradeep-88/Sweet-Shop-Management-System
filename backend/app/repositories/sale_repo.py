from sqlalchemy.orm import Session
from app.models.sale import Sale


class SaleRepository:

    @staticmethod
    def create(db: Session, sale: Sale):
        db.add(sale)
        db.commit()
        db.refresh(sale)
        return sale

    @staticmethod
    def get_all(db: Session):
        return db.query(Sale).all()
