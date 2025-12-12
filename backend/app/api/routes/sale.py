from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.api.deps import get_current_user
from app.core.roles import require_admin
from app.models.user import User
from app.schemas.sale import SaleCreate, SaleOut
from app.services.sale_service import SaleService
from app.repositories.sale_repo import SaleRepository

router = APIRouter(prefix="/sales", tags=["Sales"])


# Staff can sell sweets
@router.post("/", response_model=SaleOut)
def sell_sweet(
    sale: SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SaleService.sell(
        db=db,
        sweet_id=sale.sweet_id,
        quantity=sale.quantity,
        sold_by=current_user.id,
    )


# Admin can view all sales
@router.get("/", response_model=List[SaleOut])
def list_sales(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    return SaleRepository.get_all(db)
