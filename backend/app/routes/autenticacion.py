from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.utils.seguridad import verify_password, get_password_hash, create_access_token
from app.utils.settings import Settings
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

class UserCreate(BaseModel):
    email: str
    password: str
    role: str = "owner"

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user: raise HTTPException(400, "Email ya registrado")
    hashed = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed, role=user.role)
    db.add(db_user); db.commit(); db.refresh(db_user)
    token = create_access_token(data={"sub": db_user.email, "scopes": [user.role]}, expires_delta=timedelta(minutes=Settings.access_token_expires_m))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password): 
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token(data={"sub": user.email, "scopes": [user.role]})
    return {"access_token": token, "token_type": "bearer"}
