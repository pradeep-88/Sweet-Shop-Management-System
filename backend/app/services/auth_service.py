from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.repositories.user_repo import UserRepository
from app.models.user import User
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def register(
        db: Session,
        email: str,
        password: str,
        role: str = "staff",
    ):
        user = User(
            email=email,
            hashed_password=AuthService.hash_password(password),
            role=role,
        )
        return UserRepository.create(db, user)

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserRepository.get_by_email(db, email)
        if not user:
            return None

        if not AuthService.verify_password(password, user.hashed_password):
            return None

        return create_access_token({"sub": user.email})
