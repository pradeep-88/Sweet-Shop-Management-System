from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.api.deps import get_current_user
from app.core.roles import require_admin
from app.models.user import User
from app.schemas.sweet import SweetCreate, SweetUpdate, SweetOut
from app.services.sweet_service import SweetService

router = APIRouter(prefix="/sweets", tags=["Sweets"])


@router.post("/", response_model=SweetOut)
def create_sweet(
    sweet: SweetCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    return SweetService.create(db, sweet)


@router.get("/", response_model=List[SweetOut])
def list_sweets(
    name: str | None = Query(default=None),
    category: str | None = Query(default=None),
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SweetService.list(
        db=db,
        name=name,
        category=category,
        min_price=min_price,
        max_price=max_price,
        skip=skip,
        limit=limit,
    )


@router.get("/{sweet_id}", response_model=SweetOut)
def get_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SweetService.get(db, sweet_id)


@router.put("/{sweet_id}", response_model=SweetOut)
def update_sweet(
    sweet_id: int,
    sweet: SweetUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    return SweetService.update(db, sweet_id, sweet)


@router.delete("/{sweet_id}")
def delete_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    return SweetService.delete(db, sweet_id)
