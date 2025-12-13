from passlib.context import CryptContext
from app.repositories.user_repo import UserRepository
from app.models.user import User
from app.core.security import create_access_token
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


class AuthService:
    oauth2_scheme = oauth2_scheme

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def register(db, email: str, password: str, role: str = "staff"):
        existing_user = UserRepository.get_by_email(db, email)
        if existing_user:
            return None

        user = User(
            email=email,
            hashed_password=AuthService.hash_password(password),
            role=role,
        )
        return UserRepository.create(db, user)

    @staticmethod
    def login(db, email: str, password: str):
        repo = UserRepository(db)
        user = repo.get_by_email(email)

        if not user:
            return None

        if not user.hashed_password:
            return None

        if not AuthService.verify_password(password, user.hashed_password):
            return None

        return create_access_token({"sub": user.email})
