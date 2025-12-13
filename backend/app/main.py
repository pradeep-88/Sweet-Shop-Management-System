from fastapi import FastAPI, Depends

from app.api.routes import auth

from app.api.routes import sweet

from app.api.routes import sale




app = FastAPI(title="Sweet Shop Management System")

app.include_router(auth.router)
app.include_router(sweet.router)
app.include_router(sale.router)




@app.get("/health")
def health_check():
    return {"status": "ok"}

from app.api.deps import get_current_user
from app.models.user import User


@app.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role,
    }


