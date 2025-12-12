from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# IMPORTANT: import models here so Alembic detects them
from app.models.user import User  # noqa
from app.models.sweet import Sweet  # noqa
